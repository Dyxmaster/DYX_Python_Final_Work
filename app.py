from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import torch
from torchvision import transforms
from PIL import Image
from resnet import load_model  # 导入 load_model 函数
import os
from SQLmodels import User
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import config
import json

# 创建应用实例
app = Flask(__name__)
app.secret_key = 'DYXKING'  # 设置一个安全的 secret key

# 配置文件
app.config.from_object(config)

# 初始化数据库
from exts import db
db.init_app(app)

# 初始化迁移
migrate = Migrate(app, db)

# 注册蓝图
from blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)

# 文件上传路径
UPLOAD_FOLDER = 'static/uploads'  # 修改为静态目录
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 加载模型
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = load_model("./model/model.pth", num_classes=176)  # 使用 resnet_model.py 中的 load_model 函数

# 加载类别标签
with open('./model/label_mapping.json', 'r') as f:
    label_mapping = json.load(f)

# 定义图片预处理转换
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.ToTensor(),  # 转换为 Tensor
])

# 检查文件类型
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 登录页面视图
@app.route('/')
def login():
    return render_template('login.html')

# 登录处理
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('name')
    password = request.form.get('pass')
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return redirect(url_for('index'))
    else:
        flash('用户名或密码错误，请重试！')
        return redirect(url_for('login'))

# 注册页面处理
@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form.get('regname')
    password = request.form.get('regpass')
    password_confirm = request.form.get('reregpass')

    if password != password_confirm:
        flash('两次输入的密码不一致，请重试！')
        return redirect(url_for('login'))

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('用户名已存在，请选择另一个用户名')
        return redirect(url_for('login'))

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=hashed_password, created_time=datetime.now())
    db.session.add(new_user)
    db.session.commit()

    flash('注册成功，请登录！')
    return redirect(url_for('login'))

# 用户管理页面
@app.route('/users')
def users():
    user_list = User.query.all()
    return render_template('users.html', users=user_list)

# 删除用户
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('用户删除成功！')
    else:
        flash('用户不存在！')
    return redirect(url_for('users'))

# 主页面
@app.route('/index')
def index():
    return render_template('index.html')

# 图像分类页面
@app.route('/classify', methods=['GET', 'POST'])
def classify():
    filename = None
    predicted_class = None
    predicted_label = None
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('没有文件上传！')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('没有选择文件！')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # 检查是否存在上传文件夹，如果不存在则创建
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            file.save(file_path)

            # 加载图片并进行预处理
            img = Image.open(file_path)
            img = transform(img).unsqueeze(0).to(device)

            # 使用模型进行分类
            with torch.no_grad():
                output = model(img)
                _, predicted = torch.max(output, 1)

            predicted_class = predicted.item()

            # 获取实际的类别标签
            predicted_label = label_mapping[predicted_class]

            flash(f'预测结果: 类别 {predicted_class} - {predicted_label}')

            return render_template('classify.html', filename=filename, predicted_class=predicted_class, predicted_label=predicted_label)

    return render_template('classify.html', filename=filename, predicted_class=predicted_class, predicted_label=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)

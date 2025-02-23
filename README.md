# 一、项目背景  
本项目最初作为期末作业开展，旨在利用深度学习技术解决实际应用问题。具体而言，希望将其应用于林区无人机系统，通过对树叶种类的准确预测来识别树木，进而对珍稀树种进行有效保护，防止其灭绝，为森林生态保护提供有力的技术支持。        
# 二、项目概述   
这是一个基于残差网络（ResNet）实现的树叶分类项目。项目运用深度学习模型，能够对不同种类的树叶进行自动分类。同时，采用 Flask 作为前后端框架，构建了一个 Web 应用接口，方便用户上传树叶图片并获取分类结果。ResNet 的残差模块有效解决了深度网络训练中的梯度消失问题，显著提升了模型的性能和分类准确率。本项目不仅展示了深度学习在植物分类领域的应用潜力，还为用户提供了一个便捷易用的树叶分类工具。            
# 三、项目结构  
项目主要由以下文件夹和文件构成：   
文件夹 / 文件名	描述    
.idea	此文件夹是 IntelliJ IDEA 等开发工具的专属配置目录，存放着与项目相关的各种设置信息，这些信息对开发环境的配置和项目的运行起着关键作用，通常在开发过程中由工具自动生成和管理        
blueprints	该文件夹用于存放 Flask 蓝图相关代码。Flask 蓝图是一种组织和管理应用功能模块的有效方式，通过将不同功能的代码分离到各个蓝图中，使得项目代码结构更加清晰，增强了代码的可读性和可维护性，同时也方便了项目的扩展        
leafclass	存放与树叶分类紧密相关的自定义类或函数。这些类和函数在数据预处理、模型训练辅助等方面发挥重要作用，是实现树叶分类功能的重要组成部分     
migrations	主要用于数据库迁移操作。在项目开发过程中，当数据库结构需要进行变更（如添加新表、修改字段等）时，该文件夹下的脚本能够帮助同步更新数据库，确保数据库结构与代码中的模型定义保持一致，保证数据的完整性和一致性         
model	存放训练好的模型文件，或者包含与模型定义、加载、保存等操作相关的代码。这些代码负责管理模型的生命周期，使得训练好的模型能够在项目中被正确加载和使用，为树叶分类提供核心支持        
static	专门用于存放静态资源文件，例如 CSS 样式表、JavaScript 脚本、图片等。这些静态资源文件能够美化 Web 应用的界面，增强用户交互体验，使应用更加美观和易用    
templates	存放 HTML 模板文件，Flask 框架借助这些模板来生成动态网页内容。通过模板引擎，开发人员可以将动态数据与 HTML 模板相结合，生成个性化的网页，为用户提供丰富的交互界面   
README.md	即本文件，它详细记录了项目的关键信息，包括项目背景、概述、结构、使用方法、依赖等内容，是了解和使用该项目的重要指南   
SQLmodels.py	用于定义与 SQL 数据库相关的模型类。这些模型类与数据库表相对应，通过它们可以方便地进行数据库表的创建、数据存储和查询等操作，是项目与数据库交互的关键代码文件
app.py	作为项目的主应用文件，承担着初始化 Flask 应用、定义路由、处理用户请求和响应等核心功能。它是整个 Web 应用的核心控制中枢，负责协调各个模块之间的工作，确保用户请求能够得到正确处理并返回相应的结果   
config.py	主要存放项目的各种配置信息，例如数据库连接字符串、Flask 应用的密钥、模型训练参数等。将配置信息集中存放在此文件中，方便对项目进行统一配置和管理，提高了项目的可维护性和可扩展性   
exts.py	可能包含扩展相关的代码，用于初始化和配置项目中使用的各种扩展库。例如，在项目中使用数据库连接扩展、表单验证扩展等时，相关的初始化和配置代码可能会放在这个文件中，确保扩展库能够在项目中正常工作   
resnet.py	该文件实现了残差网络（ResNet）的相关代码，包含 ResNet 模型的网络结构定义、前向传播等重要功能。ResNet 模型的有效实现是本项目实现高精度树叶分类的核心技术支撑   
# 四、数据集
受文件上传限制，当前仓库仅包含部分数据集，约 4 万多张树叶图片未上传。若需要完整数据集，请联系我。  
# 五、技术实现
深度学习模型：项目采用残差网络（ResNet）作为核心深度学习模型。ResNet 的创新之处在于其独特的残差模块，该模块通过引入捷径连接（shortcut connection），使得网络在训练过程中能够更有效地传递梯度，避免了梯度消失问题。这一特性使得 ResNet 能够构建更深层次的网络结构，从而学习到更复杂、更具代表性的树叶特征，极大地提升了模型对树叶分类的准确率和整体性能。     
Web 框架：选择 Flask 框架搭建前后端交互的 Web 应用接口。Flask 是一个轻量级且灵活的 Python Web 框架，它提供了简洁易用的路由系统，方便开发人员定义不同的 URL 路径及其对应的处理函数，实现对用户请求的精准处理。同时，Flask 的模板渲染功能强大，能够方便地将动态数据与 HTML 模板相结合，生成丰富多样的网页内容，为用户提供良好的交互体验。      
 

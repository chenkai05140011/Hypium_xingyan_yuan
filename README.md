HypiumProjectTemplate

HypiumTest

     aw                                       // 工程中自定义模块文件夹
    
            Utils.py                         // 示例模块文件
    
     config                                  // 测试工程配置文件夹
    
            user_config.xml             // 测试工程配置文件，主要是测试框架的任务配置
    
    resource                              // 测试资源文件夹，测试过程中用到的资源文件默认会优先从当前文件夹进行查找
    
            images            // 资源文件子目录
    
                icon_mms.png   // 资源文件，以png图片为例
    
    testcases                             // 测试用例文件夹，测试过程中的测试用例文件优先会从当前文件夹进行查找
    
            Example.json                  // Example测试用例配置文件，配置用例设备信息等
            
            Example.py                     // Example测试用例文件，实际的测试逻辑代码
    
    MANIFEST.in                // 声明脚本执行过程中需要用到的aw包 
    
    setup-regression.py                // 声明用例

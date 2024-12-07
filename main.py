from xdevice.__main__ import main_process

if __name__ == "__main__":
    # 执行testcases下的Example.py用例
    # main_process("run -l Home_page -l Play_details_page -ta agent_mode:bin;screenshot:true")
    main_process(
      "run -l Home_page;Play_details_page;Theater_page;History_page;Welfare_page;My_page -ta agent_mode:bin;screenshot:true"
    )
    # run --retry --session 2022-12-13-12-21-11(report任务报告目录)
    # main_process(
    #     "run --retry --session 2024-12-07-09-12-48"
    # )



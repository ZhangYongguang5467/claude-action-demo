# Claude Code Action Demo

测试 GitHub Issue 触发 Claude AI 自动生成代码并创建 PR。

## 使用方法

在 Issue 中评论 `@claude` 并描述你的需求，例如：

```
@claude 请帮我在 utils.py 中添加一个计算阶乘的函数
```

## 项目结构

```
├── src/
│   ├── main.py      # 主程序
│   └── utils.py     # 工具函数
└── .github/
    └── workflows/
        └── claude.yml  # Claude Action 配置
```

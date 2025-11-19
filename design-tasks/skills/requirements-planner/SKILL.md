---
name: requirements-planner
description: 理清用户需求并确认技术方案的 Skill。使用 AskUserQuestion 工具与用户进行澄清对话，理解开发意图，设计可行的技术方案并让用户确认。
---

# Requirements Planner

## 概述

这个 Skill 专门负责理清用户的开发需求和意图，并根据需求设计可行的技术方案。它会通过 AskUserQuestion 工具与用户进行澄清对话，确保准确理解用户意图，然后提供至少两种可行的技术方案供用户选择。

## 使用场景

当用户使用 `/dt` 或 `/dt-design` 命令时，这个 Skill 会在第一阶段被调用，用于：
1. 理解用户提供的开发需求或意图
2. 澄清模糊或不明确的意图
3. 设计至少两种可行的技术方案
4. 引导用户选择一个方案
5. 输出清晰的需求和方案确认

## 工作流程

### 第 1 步：理解初始需求

分析用户提供的开发需求或意图：
- 如果意图明确，直接进入第 2 步设计方案
- 如果意图不明确，必须一次性提出所有必要的澄清问题

### 第 2 步：方案设计与选择

基于理解，设计至少两种可行的技术方案：

1. **详细描述每个方案**：
   - 核心思想和实现路径
   - 大致的技术栈和架构
   - 关键特性和优势

2. **对比分析**：
   - 使用表格从多个维度对比方案优缺点
   - 维度包括：实现复杂度、性能、可维护性、扩展性、优点、缺点

3. **推荐方案**：
   - 明确推荐一个方案
   - 详细阐述推荐理由（基于项目阶段、技术栈匹配度、长期规划等）

### 第 3 步：用户确认

使用 AskUserQuestion 工具引导用户：
1. 回答澄清问题（如有）
2. 从设计方案中选择一个方案
3. 确认方案描述是否准确

### 第 4 步：输出结果

输出格式化的确认结果：
- 理清后的需求描述
- 选择的方案详情
- 方案的关键实现要点

## AskUserQuestion 使用方式

每次与用户对话时，使用 AskUserQuestion 工具。**重要**：应该将所有需要澄清的问题一次性提出，每个问题都有自己独立的选项列表。

**多个澄清问题示例（推荐方式）**：
```
{
  "questions": [
    {
      "question": "请选择您偏好的技术方案：",
      "header": "技术方案",
      "options": [
        {"label": "方案 A：Golang + React", "description": "高性能，适合高并发场景"},
        {"label": "方案 B：Python + Django", "description": "开发效率高，适合快速迭代"}
      ],
      "multiSelect": false
    },
    {
      "question": "请选择您偏好的数据库：",
      "header": "数据库",
      "options": [
        {"label": "PostgreSQL", "description": "功能强大，支持复杂查询"},
        {"label": "MySQL", "description": "成熟稳定，社区支持好"},
        {"label": "MongoDB", "description": "灵活的文档数据库"}
      ],
      "multiSelect": false
    },
    {
      "question": "关于用户认证系统，您希望支持哪些登录方式？",
      "header": "登录方式",
      "options": [
        {"label": "用户名密码", "description": "传统的用户名密码登录"},
        {"label": "邮箱验证", "description": "发送验证码到邮箱登录"},
        {"label": "OAuth登录", "description": "Google、GitHub等第三方登录"},
        {"label": "短信验证", "description": "通过手机短信验证码登录"}
      ],
      "multiSelect": true
    }
  ]
}
```

**单个问题示例（简单场景）**：
```
{
  "questions": [
    {
      "question": "请选择您偏好的技术方案：",
      "header": "方案选择",
      "options": [
        {"label": "方案 A：JWT + Redis 方案", "description": "性能更好，适合高并发场景"},
        {"label": "方案 B：Session 方案", "description": "实现简单，适合小型应用"}
      ],
      "multiSelect": false
    }
  ]
}
```

## 输出格式

返回的结构化信息应包含：
- **需求描述**：清晰、准确的用户需求总结
- **技术方案**：用户选择的具体方案
- **方案详情**：方案的详细描述、优缺点、推荐理由
- **澄清结果**：所有澄清问题的答案

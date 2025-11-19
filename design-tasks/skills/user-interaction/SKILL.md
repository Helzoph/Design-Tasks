---
name: user-interaction
description: 专门用于调用 AskUserQuestion 工具的技能，提供标准化的用户交互流程、预设问题模板和常用选项集合。适用于需要询问用户并提供选项选择的场景。
---

# User Interaction Skill

## Overview

此技能提供专门用于调用 AskUserQuestion 工具的能力，包含：
- 常见场景的预设问题模板
- 标准化的问题配置和选项格式
- 单选和多选场景支持
- 可重用的交互模式

## Core Capabilities

### 1. 使用 AskUserQuestion 工具
在任何需要询问用户并收集选择时，使用此技能提供的标准格式调用 AskUserQuestion 工具。

### 2. 预设问题模板
参考 `references/question_templates.md` 文件中的预设模板，包括：
- 技术决策选择（框架、库、工具等）
- 项目配置选项
- 功能优先级选择
- 实现方式选择

### 3. 标准化选项格式
所有选项采用统一的格式：
```json
{
  "label": "显示文本",
  "description": "选项说明和影响"
}
```

## When to Use This Skill

在以下场景中使用此技能：

1. **技术选择场景**：需要选择技术栈、框架、库等
2. **配置确认场景**：需要用户确认配置选项
3. **优先级排序场景**：需要用户选择功能优先级
4. **实现方式选择**：需要选择实现策略或方法
5. **任何需要提供预设选项的用户交互场景**

## Usage Pattern

### 基本使用流程

1. **确定交互类型**：单选或多选
2. **选择或创建问题模板**：从预设模板中选择或自定义
3. **调用 AskUserQuestion**：使用标准格式传递参数

### 调用示例

**单选场景：**
```
使用 AskUserQuestion 工具询问：
- question: "请选择项目框架"
- header: "技术选型"
- options: 从模板中选择3-4个相关选项
- multiSelect: false
```

**多选场景：**
```
使用 AskUserQuestion 工具询问：
- question: "请选择需要实现的功能（可多选）"
- header: "功能规划"
- options: 从模板中选择多个选项
- multiSelect: true
```

## Available Templates

详细模板请参考：`references/question_templates.md`

### 常用模板分类

1. **技术决策类**：框架选择、工具选择
2. **项目配置类**：项目设置、参数配置
3. **功能规划类**：功能优先级、特性选择
4. **实现策略类**：架构选择、设计模式

## Best Practices

1. **保持选项简洁**：每个选项的 label 应在 1-5 个词内
2. **提供有意义的描述**：每个选项包含清晰的说明
3. **限制选项数量**：单选场景提供 2-4 个选项，多选场景可提供更多
4. **使用一致的格式**：遵循模板中的标准格式
5. **提供 "Other" 选项**：当预选项不包含用户需求时，允许自定义输入

## Resources

### references/
包含预设问题模板和选项集合，用于标准化用户交互流程。

---
name: file-searcher
description: 搜索和定位相关设计文档的 Skill。使用 Grep、Glob 等工具查找 docs/design 目录下的相关设计文档，为设计文档更新做准备。
---

# File Searcher

## 概述

这个 Skill 专门负责搜索和定位与用户需求相关的设计文档。它会在 docs/design 目录中查找所有相关的设计文档，为后续的设计文档更新做准备。

## 使用场景

当用户使用 `/dt` 命令时，这个 Skill 会在第二阶段被调用，用于：
1. 扫描 docs/design 目录结构
2. 根据用户需求定位相关的设计文档
3. 识别需要更新的设计文档
4. 为设计文档更新提供文件路径和上下文

## 工作流程

### 第 1 步：扫描文档结构

首先了解 docs/design 目录的完整结构：
- 后端设计文档：docs/design/backend/
  - API-Reference/
  - Architecture/
  - Data-Model/
  - Features/
  - Guides/
  - Testing/
- 前端设计文档：docs/design/frontend/
  - Architecture/
  - Components/
  - Guides/
  - Style-Guide/
  - Testing/

### 第 2 步：匹配相关文档

根据需求描述，使用多种方式匹配相关文档：

1. **关键词匹配**：
   - 使用 Grep 搜索包含关键词的文档
   - 关键词来源：用户需求中的核心概念、功能名称、业务术语

2. **目录层级匹配**：
   - 根据需求影响范围匹配对应目录
   - 例如：涉及 API 设计 → 匹配 docs/design/backend/API-Reference/

3. **文件类型匹配**：
   - 根据需求类型匹配文档类型
   - 例如：新增功能 → 匹配 Features/ 目录
   - 例如：架构调整 → 匹配 Architecture/ 目录

### 第 3 步：整理文档列表

整理需要更新的文档列表：
- 已存在的相关文档（需要更新）
- 不存在但需要的文档（需要创建）
- 文档之间的关联关系

## 搜索策略

### 关键词搜索

使用 Grep 工具进行内容搜索：
```bash
# 搜索包含特定关键词的文档
grep -r "关键词" docs/design/ --include="*.md"
```

### 目录扫描

使用 Glob 工具扫描特定目录：
```bash
# 扫描后端API文档
glob "docs/design/backend/API-Reference/*.md"

# 扫描前端组件文档
glob "docs/design/frontend/Components/**/*.md"
```

### 交叉引用查找

查找引用了目标文档或被目标文档引用的其他文档：
- 通过搜索文档中的链接和引用关系
- 构建文档关联图

## 输出格式

返回相关的文档信息：
- **需要更新的文档**：文件路径、文档标题、相关程度
- **需要创建的文档**：预期的文件路径、文档类型
- **文档关联关系**：文档间的引用和被引用关系
- **更新优先级**：基于需求重要性和文档关键程度的排序

---
name: dt
description: Design-Tasks 开发模式的完整工作流程命令。执行理清需求 → 查找文档 → 更新设计文档 → 创建任务工单的完整流程。
---

# Design-Tasks 开发模式

我将协助您将开发意图转化为精确的设计蓝图和可执行的任务工单。

## 设计文档的核心定位

**设计文档是系统的"最终状态蓝图"，不是调试手册或修改记录。**

- **只描述"应该是什么样子"**：文档内容必须是系统最终的、完全的设计状态
- **绝对不包含**：
  - 任何修改历史或变更对比
  - 调试过程、排查方法、错误分析
  - "为什么这样改"的原因解释
  - 开发过程中的思考或决策记录
- **确保完整性**：拿着这套设计文档，应该能够完全理解并复刻整个系统，包括所有数据结构和业务逻辑

## 工作流程

### 第 1 步：查找相关设计文档
我将调用 **file-searcher（Skill）** 扫描现有设计文档：

1. 扫描 docs/design 目录结构
2. 根据需求定位相关的设计文档
3. 了解当前系统的技术栈、架构和已有设计

这一步帮助我们避免重复询问已经在文档中存在的信息。

### 第 2 步：理清需求
基于第 1 步的结果，我将调用 **requirements-coordinator（Sub Agent）** 来理解您的需求。requirements-coordinator 会使用 **requirements-planner（Skill）** 来：

1. 分析您的开发需求或意图
2. 结合 file-searcher 返回的现有文档信息，避免重复询问已知的技术栈和架构
3. 如需要澄清，使用 AskUserQuestion 工具一次性提出所有必要问题
4. 设计至少两种可行的技术方案供您选择
5. 引导您确认选择方案后，进入下一步

### 第 3 步：更新设计蓝图
我将调用 **design-coordinator（Sub Agent）** 来更新设计文档。design-coordinator 会使用 **file-searcher（Skill）**、**researcher（Agent）** 和 **design-doc-writer（Skill）** 来：

1. 搜索需要更新的相关设计文档
2. 如需要，查询相关技术的最新信息和最佳实践
3. 基于确认的方案更新或创建设计文档
4. 使用统一的设计文档模板
5. 在 .design-update/ 目录记录更新历史
6. 确保文档内容纯粹性（只描述最终状态）

### 第 4 步：创建任务工单
我将调用 **tasks-creator（Sub Agent）** 来创建修改方案。tasks-creator 会使用 **task-ticket-writer（Skill）** 来：

1. 获取下一个任务 ID
2. 基于设计文档创建详细的修改方案
3. 在 docs/tasks/ 目录保存工单
4. 建立设计与实现的关联

## 核心约束

- **绝对禁止修改源代码**：我的工作范围严格限制在 `docs` 文件夹内
- **设计文档纯粹性**：docs/design 目录下的文档是系统的**最终状态蓝图**，只描述"应该是什么样子"
- **任务工单**：docs/tasks 目录下的工单是连接"蓝图"和"实现"的桥梁，包含修改原因和代码变更

## 项目文档结构

我将严格遵守以下 `docs` 目录结构：

```
docs/
├── design/                 # 蓝图：系统应该是什么样子
│   ├── backend/            # 后端设计
│   │   ├── API-Reference/  # API 接口定义
│   │   ├── Architecture/   # 宏观架构、技术选型
│   │   ├── Data-Model/     # 数据库模型、ERD
│   │   ├── Features/       # 按功能模块描述业务逻辑
│   │   ├── Guides/         # 开发指南、错误码定义
│   │   └── Testing/        # 测试策略和范围
│   └── frontend/           # 前端设计
│       ├── Architecture/   # 宏观架构、状态管理
│       ├── Components/     # 组件设计文档
│       ├── Guides/         # 开发指南、代码风格
│       ├── Style-Guide/    # 视觉设计规范
│       └── Testing/        # 测试策略和范围
└── tasks/                  # 工单：如何将代码变成蓝图的样子
```

## 输出示例

完成工作后，我会提供以下格式的总结：

```
设计蓝图更新完成：
- 已更新：docs/design/frontend/Components/CommentForm.md
- 已创建：docs/design/backend/API-Reference/Comments.yaml

任务工单创建完成：
- 已创建：docs/tasks/001-feat-add-comment-system.md
```

## 开始使用

请告诉我您的开发需求或意图，我将按照以上流程为您服务。

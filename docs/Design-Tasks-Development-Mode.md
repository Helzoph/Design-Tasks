# Design-Tasks 开发模式

## 概述

Design-Tasks 是一个文档驱动的软件开发工作流程模式，旨在通过系统化的设计文档和任务工单管理，实现从需求到实现的规范化转换。该模式将设计与实现明确分离，确保开发过程的可追溯性和系统的可维护性。

## 工作流程的核心改进

**重要变更**：所有命令流程的第一步都调整为"查找文档"，第二步才是"理清需求"。

**原因**：先了解现有系统状态（技术栈、架构、已有设计），再基于这些信息理清需求，可以避免重复询问已经在文档中明确的信息，提升开发效率。

**优势**：
- 避免重复询问技术栈（如"前端用什么框架？"、"后端用什么语言？"）
- 避免重复询问架构信息（如"采用什么架构模式？"、"数据库选型？"）
- 基于现有设计进行增量开发，保持文档一致性
- 提升需求澄清的效率和准确性

## 核心理念

### 1. 设计文档的纯粹性

**设计文档是系统的"最终状态蓝图"，而非调试手册或修改记录。**

- **只描述"应该是什么样子"**：文档内容必须是系统最终的、完全的设计状态
- **绝对不包含**：
  - 任何修改历史或变更对比
  - 调试过程、排查方法、错误分析
  - "为什么这样改"的原因解释
  - 开发过程中的思考或决策记录
- **确保完整性**：拿着这套设计文档，应该能够完全理解并复刻整个系统，包括所有数据结构和业务逻辑

### 2. 双层架构

```
┌─────────────────────────────────────────┐
│            docs/design/                 │
│         (系统蓝图 - 只读)                │
│  描述系统最终应该是什么样子               │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│            docs/tasks/                  │
│       (实现方案 - 可执行)                │
│  描述如何将代码变成蓝图的样子             │
└─────────────────────────────────────────┘
```

- **design/**：系统最终状态的完整蓝图
- **tasks/**：基于蓝图衍生的可执行任务工单

## 工作流程

Design-Tasks 开发模式提供三种工作流程，适应不同的开发场景：

### 流程 1：完整流程 (`/dt`)

```
查找文档 → 理清需求 → 更新设计文档 → 创建任务工单
```

**适用场景**：全新功能开发或重大架构调整

**关键优势**：先了解现有系统状态，避免重复询问已经在文档中明确的技术栈和架构信息

### 流程 2：设计文档更新 (`/dt-design`)

```
查找文档 → 理清需求 → 更新设计文档
```

**适用场景**：
- 只需要更新或创建设计文档
- 设计方案的讨论和分析
- 架构调整和文档同步

**关键优势**：先了解现有文档，避免重复询问已知信息

### 流程 3：任务工单创建 (`/dt-tasks`)

```
查找文档 → （理清需求） → 创建任务工单
```

**适用场景**：
- 只需要创建任务工单
- 现有设计文档需要转化为实现方案
- 将设计转化为可执行的代码变更指南

**关键优势**：基于现有设计文档创建任务工单，避免重复询问已在文档中明确的信息。理清需求步骤在此流程中是可选的。

## 命令详解

### `/dt` - 完整开发流程

**执行步骤**：

1. **查找相关设计文档**
   - 调用 `file-searcher` Skill
   - 扫描 `docs/design` 目录结构
   - 定位相关的设计文档
   - 了解当前系统的技术栈、架构和已有设计

2. **理清需求**
   - 调用 `requirements-coordinator` Sub Agent（使用 `requirements-planner` Skill）
   - 结合现有文档信息，避免重复询问已知的技术栈和架构
   - 分析开发需求或意图
   - 提出澄清问题（如需要）
   - 设计至少两种可行的技术方案
   - 用户确认技术方案

3. **更新设计蓝图**
   - 调用 `design-coordinator` Sub Agent（使用 `file-searcher`、`researcher` 和 `design-doc-writer` Skills）
   - 如需要，查询相关技术的最新信息和最佳实践
   - 基于确认的方案更新或创建设计文档
   - 使用统一的设计文档模板
   - 在 `.design-update/` 目录记录更新历史
   - 确保文档内容纯粹性

4. **创建任务工单**
   - 调用 `tasks-creator` Sub Agent（使用 `task-ticket-writer` Skill）
   - 获取下一个任务 ID
   - 基于设计文档创建详细的修改方案
   - 在 `docs/tasks/` 目录保存工单
   - 建立设计与实现的关联

**关键改进**：第 1 步先了解现有系统状态，第 2 步基于这些信息理清需求，避免重复询问已经在文档中存在的信息。

### `/dt-design` - 设计文档更新

专注于设计文档的更新，不创建任务工单。

**执行步骤**：

1. **查找相关设计文档**
   - 调用 `file-searcher` Skill
   - 扫描 `docs/design` 目录结构
   - 定位相关的设计文档
   - 了解当前系统的技术栈、架构和已有设计

2. **理清需求**
   - 调用 `requirements-coordinator` Sub Agent（使用 `requirements-planner` Skill）
   - 结合现有文档信息，避免重复询问已知的技术栈和架构
   - 分析开发需求或意图
   - 提出澄清问题（如需要）
   - 设计至少两种可行的技术方案
   - 用户确认技术方案

3. **更新设计蓝图**
   - 调用 `design-coordinator` Sub Agent（使用 `file-searcher`、`researcher` 和 `design-doc-writer` Skills）
   - 如需要，查询相关技术的最新信息和最佳实践
   - 基于确认的方案更新或创建设计文档
   - 使用统一的设计文档模板
   - 在 `.design-update/` 目录记录更新历史
   - 确保文档内容纯粹性

**关键约束**：
- 绝对禁止修改源代码
- 工作范围严格限制在 `docs` 文件夹内
- 不创建 `docs/tasks` 目录下的工单文件

### `/dt-tasks` - 任务工单创建

基于现有设计文档创建可执行的任务工单。

**执行步骤**：

1. **查找相关设计文档**
   - 调用 `file-searcher` Skill
   - 扫描 `docs/design` 目录结构
   - 定位相关的设计文档
   - 了解当前系统的技术栈、架构和已有设计

2. **理清需求（可选）**
   - 如果需要澄清具体实现细节，调用 `requirements-coordinator` Sub Agent（使用 `requirements-planner` Skill）
   - 结合现有文档信息，避免重复询问已知的技术栈和架构
   - 对于已明确的需求（如修复现有 Bug），可直接跳过此步骤

3. **创建任务工单**
   - 调用 `tasks-creator` Sub Agent（使用 `task-ticket-writer` Skill）
   - 获取下一个任务 ID
   - 基于设计文档创建详细的修改方案
   - 在 `docs/tasks/` 目录保存工单
   - 建立设计与实现的关联

**关键约束**：
- 不更新 `docs/design` 目录下的文档
- 依赖现有的设计文档来创建任务工单
- 工单文件命名格式：`<id>-<type>-<task_description>.md`

## 文档结构规范

### 标准目录结构

```
docs/
├── design/                      # 蓝图：系统应该是什么样子
│   ├── backend/                 # 后端设计
│   │   ├── API-Reference/       # API 接口定义
│   │   ├── Architecture/        # 宏观架构、技术选型
│   │   ├── Data-Model/          # 数据库模型、ERD
│   │   ├── Features/            # 按功能模块描述业务逻辑
│   │   ├── Guides/              # 开发指南、错误码定义
│   │   └── Testing/             # 测试策略和范围
│   └── frontend/                # 前端设计
│       ├── Architecture/        # 宏观架构、状态管理
│       ├── Components/          # 组件设计文档
│       ├── Guides/              # 开发指南、代码风格
│       ├── Style-Guide/         # 视觉设计规范
│       └── Testing/             # 测试策略和范围
├── tasks/                       # 工单：如何将代码变成蓝图的样子
│   ├── 001-feat-add-comment-system.md
│   ├── 002-fix-login-bug.md
│   └── ...
└── .design-update/              # 设计文档更新记录
    └── 2025-11-19-design-updates.md
```

### 设计文档分类

#### Backend Design
- **API-Reference**：接口定义、数据格式、响应结构
- **Architecture**：系统架构、技术选型、部署方案
- **Data-Model**：数据库设计、ERD 模型、数据关系
- **Features**：按业务模块描述的后端逻辑
- **Guides**：开发规范、错误码、调试指南
- **Testing**：测试策略、测试用例、Mock 数据

#### Frontend Design
- **Architecture**：前端架构、状态管理、路由设计
- **Components**：组件设计、Props 定义、交互逻辑
- **Guides**：代码规范、开发工具、构建配置
- **Style-Guide**：视觉规范、组件库、设计系统
- **Testing**：测试策略、E2E 测试、组件测试

### 任务工单规范

#### 文件命名

格式：`<id>-<type>-<task_description>.md`

- **id**：递增序号（001, 002, 003...）
- **type**：任务类型
  - `feat`：新功能
  - `fix`：修复问题
  - `refactor`：重构
  - `docs`：文档更新
  - `style`：样式调整
  - `test`：测试相关
- **task_description**：简短英文描述（下划线连接）

**示例**：`001-feat-add-comment-system.md`

#### 内容结构

```markdown
# <id>-<type>-<task_description>

## 修改目的与背景
<详细说明修改原因和目标>

## 涉及的设计文档
<列出相关设计文档链接>

## 修改方案
### 前端修改
<前端变更内容>

### 后端修改
<后端变更内容>
```

## 角色与组件

### Sub Agents

#### requirements-coordinator
**职责**：理清用户需求并确认技术方案
- 使用 `AskUserQuestion` 工具与用户进行澄清对话
- 理解开发意图
- 设计可行的技术方案
- 获得用户确认

#### design-coordinator
**职责**：更新设计文档
- 使用 `file-searcher` Skill 搜索相关文档
- 使用 `researcher` Agent 查询最新技术信息（如需要）
- 使用 `design-doc-writer` Skill 更新设计蓝图
- 记录更新历史
- 确保设计文档基于最新技术信息

#### researcher
**职责**：查询最新文档和技术信息
- 调用 `context7` MCP 查询官方库文档和最佳实践
- 调用 `deepwiki` MCP 查询 GitHub 项目文档和社区讨论
- 支持技术选型对比和版本对比
- 帮助排查过时技术用法
- 确保技术方案的时效性和准确性

#### tasks-creator
**职责**：创建任务工单
- 使用 `Read` 和 `Bash` 工具创建详细修改方案
- 写入 `docs/tasks/` 目录

### Skills

#### file-searcher
搜索和定位相关设计文档
- 使用 `Grep`、`Glob` 等工具查找相关文档
- 为设计文档更新做准备

#### requirements-planner
理清用户需求并确认技术方案

#### design-doc-writer
更新设计文档
- 基于用户需求和确认的方案
- 更新或创建设计文档
- 记录更新历史

#### task-ticket-writer
创建项目代码修改方案
- 基于设计文档
- 创建详细的修改方案工单
- 包含目的、背景、代码变更和设计关联

#### user-interaction
标准化用户交互流程

### Commands

- `/dt`：完整工作流程
- `/dt-design`：仅设计文档更新
- `/dt-tasks`：仅任务工单创建

## 使用示例

### 示例 1：添加评论功能

**用户输入**："我需要为博客添加评论功能"

**执行 `/dt` 命令**：

1. **查找文档**
   - 调用 `file-searcher` Skill 定位博客系统相关设计文档
   - 了解现有系统架构和技术栈
   - 识别需要更新的文档

2. **理清需求**
   - 调用 `requirements-coordinator` Sub Agent
   - 结合现有文档信息，确认评论功能的具体需求
   - 讨论技术方案（实时推送 vs 刷新加载）
   - 用户选择方案

3. **更新设计**
   - 调用 `design-coordinator` Sub Agent
   - 创建 `docs/design/backend/API-Reference/Comments.yaml`
   - 更新 `docs/design/frontend/Components/CommentForm.md`
   - 记录到 `.design-update/2025-11-19-design-updates.md`

4. **创建工单**
   - 调用 `tasks-creator` Sub Agent
   - 生成 `docs/tasks/001-feat-add-comment-system.md`
   - 包含前后端修改方案

**输出示例**：
```
设计蓝图更新完成：
- 已更新：docs/design/frontend/Components/CommentForm.md
- 已创建：docs/design/backend/API-Reference/Comments.yaml

任务工单创建完成：
- 已创建：docs/tasks/001-feat-add-comment-system.md
```

### 示例 2：修复登录 Bug

**场景**：已有登录功能设计文档，只需要创建修复工单

**执行 `/dt-tasks` 命令**：
- 基于现有登录相关设计文档
- 创建 `002-fix-login-bug.md` 任务工单
- 描述 Bug 修复的具体方案

### 示例 3：大型功能 - 电商订单系统

**用户输入**："我需要开发一个完整的电商订单系统"

这是一个复杂的大型功能，涉及多个模块：
- 订单创建和状态管理
- 支付集成
- 库存扣减
- 物流跟踪
- 订单查询和统计

**采用大型功能开发流程**：

#### 步骤 1：编写 PRD 需求文档

创建 `docs/requirements/order-system-prd.md`，包含：
- 业务目标：提升用户购物体验，实现完整的订单闭环
- 用户场景：用户浏览商品 → 下单 → 支付 → 查看物流 → 确认收货
- 功能范围：订单管理、支付流程、库存管理、物流跟踪
- 验收标准：订单创建成功率 > 99%，支付成功率 > 95%

#### 步骤 2：使用 `/dt-design` 创建设计文档

执行流程：**查找文档 → 理清需求 → 更新设计文档**

基于 PRD 文档，系统性地设计和更新文档：
- 后端设计：
  - 创建 `docs/design/backend/Architecture/OrderSystem.yaml`（整体架构）
  - 创建 `docs/design/backend/API-Reference/Orders.yaml`（订单 API）
  - 创建 `docs/design/backend/Data-Model/Order.yaml`（订单数据模型）
  - 创建 `docs/design/backend/Features/OrderWorkflow.yaml`（订单流程）

- 前端设计：
  - 创建 `docs/design/frontend/Architecture/OrderModule.yaml`（前端架构）
  - 创建 `docs/design/frontend/Components/OrderFlow.yaml`（订单流程组件）

**输出示例**：
```
设计蓝图更新完成：
- 已创建：docs/design/backend/Architecture/OrderSystem.yaml
- 已创建：docs/design/backend/API-Reference/Orders.yaml
- 已创建：docs/design/backend/Data-Model/Order.yaml
- 已更新：docs/design/frontend/Components/OrderFlow.yaml
```

#### 步骤 3：分多次使用 `/dt-tasks` 逐步实现

执行流程：**查找文档 → 创建任务工单**（理清需求步骤可选）

将订单系统拆分为 8 个独立的子任务：

**第一次实现：订单数据模型**
- 执行 `/dt-tasks`，创建 `003-feat-design-order-model.md`
- 实现：数据库表结构、实体类、关系映射

**第二次实现：订单创建流程**
- 执行 `/dt-tasks`，创建 `004-feat-create-order-flow.md`
- 实现：订单创建接口、库存校验、订单状态初始化

**第三次实现：订单查询功能**
- 执行 `/dt-tasks`，创建 `005-feat-order-query.md`
- 实现：订单列表、订单详情、状态筛选

**第四次实现：支付集成**
- 执行 `/dt-tasks`，创建 `006-feat-payment-integration.md`
- 实现：支付接口、回调处理、订单状态更新

**第五次实现：库存管理**
- 执行 `/dt-tasks`，创建 `007-feat-inventory-management.md`
- 实现：库存扣减、库存回滚、库存查询

**第六次实现：物流跟踪**
- 执行 `/dt-tasks`，创建 `008-feat-logistics-tracking.md`
- 实现：物流信息更新、物流状态同步

**第七次实现：订单前端组件**
- 执行 `/dt-tasks`，创建 `009-feat-frontend-order-components.md`
- 实现：订单列表组件、订单详情组件、状态流转组件

**第八次实现：订单统计功能**
- 执行 `/dt-tasks`，创建 `010-feat-order-statistics.md`
- 实现：订单数据统计、报表生成、分析图表

**最终输出**：
```
任务工单创建完成：
- docs/tasks/003-feat-design-order-model.md
- docs/tasks/004-feat-create-order-flow.md
- docs/tasks/005-feat-order-query.md
- docs/tasks/006-feat-payment-integration.md
- docs/tasks/007-feat-inventory-management.md
- docs/tasks/008-feat-logistics-tracking.md
- docs/tasks/009-feat-frontend-order-components.md
- docs/tasks/010-feat-order-statistics.md

完成 8 个子任务的实现，完整的电商订单系统开发完成
```

**优势**：
- 可以分配给不同的开发者并行开发
- 便于测试和验收，每个阶段都能产生可交付的价值
- 风险可控，即使某个任务延期也不影响整体进度

## 核心约束

1. **绝对禁止修改源代码**：所有工作严格限制在 `docs` 文件夹内
2. **设计文档纯粹性**：只描述最终状态，不包含调试和修改历史
3. **任务工单关联性**：工单必须关联相应的设计文档
4. **文档完整性**：设计文档应能完整描述整个系统
5. **双向追溯**：可以通过工单找到对应的设计，通过设计找到相关工单

## 优势

### 1. 职责分离
- **设计**：关注"是什么"，保证系统架构和逻辑的完整性
- **实现**：关注"怎么做"，确保代码变更的准确性和可追溯性

### 2. 可维护性
- 设计文档始终反映系统的最终状态
- 新成员可以通过设计文档快速理解整个系统
- 修改历史通过任务工单追踪

### 3. 质量保证
- 强制性的需求澄清和技术方案确认
- 标准化的文档结构和命名规范
- 设计与实现的明确关联

### 4. 协作效率
- 设计师和开发者使用统一的文档体系
- 减少沟通成本和理解偏差
- 便于 Code Review 和项目交接

## 最佳实践

### 1. 大型功能开发流程

对于复杂的大型功能，建议采用以下流程：

```
PRD 需求文档 → /dt-design 设计文档 → 多次 /dt-tasks 逐步实现
```

**具体步骤**：
1. **编写 PRD 需求文档**（Product Requirements Document）
   - 描述业务目标、用户场景、功能范围
   - 明确验收标准和成功指标
   - 存储路径：`docs/requirements/` 或项目根目录

2. **使用 `/dt-design` 创建设计文档**
   - 基于 PRD 文档进行系统设计
   - 创建完整的技术方案和架构文档
   - 更新 `docs/design/` 目录下的相关文档

3. **分多次使用 `/dt-tasks` 实现功能**
   - 将大型功能拆分为多个小的子功能
   - 每次实现一个独立的任务工单
   - 确保每个工单都是原子性的、可独立完成的任务

**优势**：
- 降低开发复杂度，每次只关注一个子功能
- 便于阶段性验收和风险控制
- 更容易进行 Code Review 和测试
- 支持并行开发（如果任务之间无依赖）

### 2. 中小型功能开发流程

对于简单的功能，可以使用简化流程：

```
/dt 完整流程 → 一次实现
```

### 3. 通用最佳实践

4. **优先设计，再实现**：新功能必须先有设计文档，再创建任务工单
5. **保持文档同步**：系统变更时及时更新设计文档
6. **工单粒度适中**：每个工单应该是原子性的、可独立完成的任务
7. **使用标准模板**：遵循统一的文档格式和命名规范
8. **记录变更原因**：在任务工单中详细说明修改的背景和目标

## 注意事项

1. **PRD 需求文档**：
   - PRD 描述"为什么做"和"做什么"，设计文档描述"怎么做"
   - PRD 是产品层面的思考，设计文档是技术层面的实现
   - 大型功能必须有 PRD 作为设计的基础

2. **设计文档不等于需求文档**：设计文档描述最终状态，需求分析在理清需求阶段完成

3. **任务工单不等于 Bug 报告**：工单包含完整的修改方案，是可执行的行动计划

4. **更新历史很重要**：`.design-update/` 目录帮助追踪设计变更，但设计文档本身不包含历史

5. **避免过度设计**：设计应该完整但不过度详细，给实现留有适当空间

6. **任务拆分原则**：
   - 如果工单过大，应该进一步拆分为多个子任务
   - 优先实现核心功能，再考虑扩展和优化

## 总结

Design-Tasks 开发模式通过将"设计"与"实现"明确分离，建立了清晰的责任边界和可追溯的开发流程。设计文档作为系统的最终状态蓝图，确保了系统的可理解性和可维护性；任务工单作为连接设计与实现的桥梁，保证了开发的可执行性和可追溯性。

这种模式特别适合：
- 中大型项目的规范化管理
- 团队协作和知识传承
- 复杂系统的长期维护
- 对代码质量有高要求的项目

通过遵循该模式的规范和流程，可以显著提升软件开发的效率和质量。
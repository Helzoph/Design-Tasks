# 项目代码结构

## 核心铁律

### 1. 禁止滥用 `README.md`
**`README.md` 仅作为目录索引，严禁将具体的设计内容（如表结构、API 定义）写入 `README.md`。**

### 2. 文件名即内容
**文件名必须精准反映其包含的业务实体或功能模块**（如 `Order.yaml`, `login-flow.md`），确保文件命名具有自描述性。

### 3. 格式分层原则
- **结构化数据 (Data Model)** 必须用 **YAML**：确保类型精确，无歧义
- **逻辑说明 (API/Features)** 必须用 **Markdown**：描述契约与交互

## 目录结构

```
<项目名称>
├── docs/
│   ├── design/  # 蓝图：系统应该是什么样子
│   │   ├── backend/  # 后端设计
│   │   │   ├── Data-Model/  # [关键] 数据库模型定义，**必须用 YAML**
│   │   │   │   ├── User.yaml       # User 实体定义
│   │   │   │   ├── Order.yaml      # Order 实体定义
│   │   │   │   └── OrderItem.yaml  # OrderItem 实体定义
│   │   │   ├── API-Reference/  # [关键] API 接口契约，**必须用 Markdown**
│   │   │   │   ├── auth-endpoints.md       # 登录/注册接口逻辑
│   │   │   │   └── payment-contract.md     # 支付回调与处理契约
│   │   │   ├── Features/  # 按功能模块描述业务逻辑，**必须用 Markdown**
│   │   │   │   └── order-state-machine.md  # 订单状态流转逻辑
│   │   │   ├── Architecture/  # 宏观架构、技术选型
│   │   │   │   └── Overview.md  # [必须] 项目总体架构说明文档
│   │   │   ├── Guides/  # 开发指南，如错误码定义、认证流程等
│   │   │   └── Testing/  # 后端测试项
│   │   └── frontend/  # 前端设计
│   │       ├── Components/  # [关键] 组件设计文档，**必须用 Markdown**
│   │       │   ├── NavBar.md           # 导航栏组件
│   │       │   └── UserProfileCard.md  # 用户信息卡片组件
│   │       ├── Architecture/  # 宏观架构、状态管理方案
│   │       │   └── Overview.md  # [必须] 项目总体架构说明文档
│   │       ├── Style-Guide/  # 视觉设计规范
│   │       └── Testing/  # 前端测试项
│   ├── manifest.json  # 自动生成的项目索引地图
│   └── tasks/  # 工单：如何将代码变成蓝图的样子
├── src/  # 源代码
│   ├── backend/  # 后端源代码
│   └── frontend/  # 前端源代码
├── tests/  # 测试文件
├── scripts/  # 脚本工具
└── README.md  # 项目说明（仅作为索引，不要写入具体设计内容）
```

## 目录与命名规范详情

### Backend Design (后端)

| 目录 | 推荐格式 | 命名规则 | 说明 |
| :--- | :--- | :--- | :--- |
| **Data-Model/** | **`.yaml`** | `<EntityName>.yaml` | **必须用 YAML**。利用 YAML 的层级特性清晰定义字段、类型、枚举、约束和索引。方便后续生成 SQL/ORM 代码。 |
| **API-Reference/** | **`.md`** | `<Module>-endpoints.md` | **必须用 Markdown**。描述接口契约、交互逻辑、关键参数和意图。**不要**生成原始的 OpenAPI/Swagger YAML（那个由代码生成）。 |
| **Features/** | `.md` | `<verb>-<noun>.md` | 描述具体业务流程、状态机或复杂算法。 |
| **Architecture/** | `.md` | `<topic>.md` | 系统概览、技术选型等。 |

### Frontend Design (前端)

| 目录 | 推荐格式 | 命名规则 | 说明 |
| :--- | :--- | :--- | :--- |
| **Components/** | `.md` | `<ComponentName>.md` | 对应具体组件名，描述 Props、State 和交互。 |
| **Architecture/** | `.md` | `<topic>.md` | 路由结构、状态管理设计等。 |

## 内容模板参考

### Data-Model (`.yaml`)
*理由：YAML 能清晰表达嵌套结构、枚举值和元数据，避免 Markdown 表格的歧义。*

```yaml
# Order.yaml
entity: Order
table: orders
columns:
  - name: status
    type: ENUM
    enum: ['pending', 'paid', 'shipped']
    default: 'pending'
  - name: total_amount
    type: DECIMAL(10,2)
    nullable: false
indexes:
  - columns: [user_id, created_at]
```

### API-Reference (`.md`)
*理由：不仅是参数列表，更重要的是描述"接口背后的意图"和"逻辑"。*

```markdown
# Auth Endpoints

## POST /login
- **功能**: 用户登录并颁发 JWT。
- **逻辑**: 校验邮箱密码 -> 更新 last_login -> 生成 Access/Refresh Token。
- **关键参数**: `email`, `password`
- **响应**: `token`, `user_info`
```

## 关键设计文档说明

### 架构设计文档（必须）

**后端架构设计必须包括：**
- `docs/design/backend/Architecture/Overview.md` - 项目总体架构说明
- 技术选型说明（框架、数据库、中间件等）
- 服务划分和模块组织
- 系统交互流程图
- 部署架构设计

**前端架构设计必须包括：**
- `docs/design/frontend/Architecture/Overview.md` - 项目总体架构说明
- 状态管理方案
- 目录结构规范
- 技术选型说明（框架、UI 库等）
- 组件架构设计

**完整性要求：** 任何一个架构模块都不应该在文档中缺失。拿着这套文档，应该能够理解整个系统的架构设计。

### 数据结构设计（必须完整覆盖）

**后端数据结构设计必须包括：**
- 所有实体（Entity）的完整定义（**用 YAML 文件**）
- 数据库表结构（字段、类型、约束）
- 实体间关系（1:1、1:N、N:M）
- 索引设计
- 数据流转逻辑

**前端数据结构设计必须包括：**
- 组件 Props/State 接口定义（**用 Markdown 文件**）
- 状态管理结构设计
- API 数据结构映射
- 缓存数据结构

**完整性要求：** 任何一个数据结构都不应该在文档中缺失。拿着这套文档，应该能够复刻整个数据模型。

# Question Templates

常用问题模板集合，每个模板包含 question、header、multiSelect 和 options。

## 技术决策类

### 前端框架选择
```json
{
  "question": "请选择项目使用的前端框架",
  "header": "前端框架选型",
  "multiSelect": false,
  "options": [
    {"label": "React", "description": "生态完善，适合大型项目"},
    {"label": "Vue.js", "description": "易上手，适合中小型项目"},
    {"label": "Angular", "description": "企业级，适合大型团队"},
    {"label": "Svelte", "description": "性能优异，追求轻量"}
  ]
}
```

### 后端技术栈选择
```json
{
  "question": "请选择项目使用的后端技术栈",
  "header": "后端技术选型",
  "multiSelect": false,
  "options": [
    {"label": "Node.js + Express", "description": "全栈开发，快速迭代"},
    {"label": "Python + FastAPI", "description": "开发效率高，文档友好"},
    {"label": "Go + Gin", "description": "高性能，适合高并发"},
    {"label": "Python + Django", "description": "全功能框架，内置管理后台"}
  ]
}
```

### 数据库选择
```json
{
  "question": "请选择项目使用的数据库类型",
  "header": "数据库选型",
  "multiSelect": false,
  "options": [
    {"label": "PostgreSQL", "description": "功能强大，适合复杂业务"},
    {"label": "MySQL", "description": "成熟稳定，通用业务场景"},
    {"label": "MongoDB", "description": "文档型，适合快速开发"},
    {"label": "SQLite", "description": "轻量级，适合小型项目"}
  ]
}
```

## 项目配置类

### 功能优先级选择（多选）
```json
{
  "question": "请选择本次迭代需要重点关注的功能（可多选）",
  "header": "功能优先级",
  "multiSelect": true,
  "options": [
    {"label": "用户认证", "description": "登录、注册、权限管理"},
    {"label": "核心业务功能", "description": "产品的核心价值功能"},
    {"label": "性能优化", "description": "提升响应速度和体验"},
    {"label": "移动端适配", "description": "优化移动设备显示"},
    {"label": "支付系统", "description": "在线支付、订单管理"}
  ]
}
```

### 部署方式选择
```json
{
  "question": "请选择项目部署方式",
  "header": "部署方案",
  "multiSelect": false,
  "options": [
    {"label": "Vercel", "description": "前端友好，自动部署"},
    {"label": "Docker + 云服务器", "description": "可控性高，可定制环境"},
    {"label": "AWS/GCP/Azure", "description": "企业级服务，功能完整"},
    {"label": "Netlify", "description": "支持 JAMstack，表单处理"}
  ]
}
```

### 项目类型选择
```json
{
  "question": "请问您想要开发什么类型的项目？",
  "header": "项目类型",
  "multiSelect": false,
  "options": [
    {"label": "Web 应用", "description": "基于浏览器的在线应用"},
    {"label": "移动应用", "description": "iOS/Android 应用"},
    {"label": "桌面应用", "description": "Windows/Mac/Linux 程序"},
    {"label": "API 服务", "description": "后端接口服务"}
  ]
}
```

## 功能规划类

### 功能模块选择（多选）
```json
{
  "question": "请选择系统需要包含的功能模块（可多选）",
  "header": "功能模块",
  "multiSelect": true,
  "options": [
    {"label": "用户管理", "description": "注册、登录、个人信息"},
    {"label": "内容管理", "description": "创建、编辑、发布内容"},
    {"label": "评论系统", "description": "评论、回复、点赞"},
    {"label": "搜索功能", "description": "搜索、筛选、排序"},
    {"label": "通知系统", "description": "消息推送、邮件通知"}
  ]
}
```

### 用户角色选择（多选）
```json
{
  "question": "请选择系统中包含的用户角色（可多选）",
  "header": "用户角色",
  "multiSelect": true,
  "options": [
    {"label": "普通用户", "description": "系统主要使用者"},
    {"label": "管理员", "description": "拥有系统管理权限"},
    {"label": "访客", "description": "未登录用户"},
    {"label": "VIP 用户", "description": "付费用户，特殊权限"}
  ]
}
```

## 实现策略类

### 认证方式选择
```json
{
  "question": "请选择用户认证方式",
  "header": "认证方式",
  "multiSelect": false,
  "options": [
    {"label": "邮箱/密码", "description": "传统方式"},
    {"label": "手机号/验证码", "description": "便捷登录"},
    {"label": "OAuth 2.0", "description": "第三方登录"},
    {"label": "无密码登录", "description": "邮件/短信链接登录"}
  ]
}
```

### API 架构风格
```json
{
  "question": "请选择 API 架构风格",
  "header": "API 架构",
  "multiSelect": false,
  "options": [
    {"label": "REST", "description": "成熟标准，缓存友好"},
    {"label": "GraphQL", "description": "灵活查询"},
    {"label": "gRPC", "description": "高性能，微服务"},
    {"label": "WebSocket", "description": "实时通信"}
  ]
}
```

### 状态管理方案
```json
{
  "question": "请选择前端状态管理方案",
  "header": "状态管理",
  "multiSelect": false,
  "options": [
    {"label": "Redux Toolkit", "description": "React 官方推荐，生态成熟"},
    {"label": "Zustand", "description": "轻量级，API 简洁"},
    {"label": "React Context", "description": "内置方案，无外部依赖"},
    {"label": "Jotai", "description": "原子化状态，现代化"}
  ]
}
```

---

## 使用说明

1. 选择适合的模板
2. 自定义问题文本和描述
3. 选择相关选项（保持 2-4 个）
4. 调用 AskUserQuestion 工具
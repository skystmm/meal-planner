# Meal Planner - 一周食谱推荐 Skill

智能生成满足家庭成员营养需求的个性化一周食谱。

## 功能特点

- ✅ 根据城市和季节推荐当季食材
- ✅ 满足不同年龄成员的营养需求
- ✅ 考虑口味偏好和忌口信息
- ✅ 保证菜品多样性（一周不重复主菜超过 3 次）
- ✅ 提供采购清单和备餐建议
- ✅ 严格避让过敏和禁忌食材

## 使用方法

### 触发方式

用户说以下关键词时自动触发：
- "生成一周食谱"
- "制定家庭饮食计划"
- "吃什么"、"食谱推荐"、"营养搭配"

### 信息收集

首次使用会引导收集以下信息：

```
📋 请提供以下信息：

1. 城市：北京、上海、广州等
2. 家庭成员：人数、年龄、性别、健康状况
3. 口味偏好：清淡/适中/重口味、辣度、其他偏好
4. 忌口信息：过敏食材、禁忌食材、不喜欢的食材
```

### 输出内容

- 📅 一周 7 天完整食谱（早餐、午餐、晚餐）
- 🛒 本周采购清单（分类列出）
- 💡 备餐建议（批量备菜、储存技巧）
- ⚠️ 注意事项（忌口提醒、营养补充）

## 目录结构

```
meal-planner/
├── SKILL.md              # 核心指令和 workflow
├── scripts/
│   └── get_season.py     # 季节判断脚本
├── references/
│   ├── nutrition-guide.md      # 家庭营养指南
│   └── nutrition-guide.md # 家庭营养指南
│
│ **季节食材**：使用 LLM 知识库实时推荐，无需固定文件
└── assets/
    └── meal-plan-template.md   # 食谱输出模板
```

## 示例输出

**用户输入**：
```
北京，家里 3 口人：爸爸 40 岁、妈妈 38 岁、孩子 8 岁
口味适中，不吃辣，孩子对海鲜过敏
```

**输出**：
```markdown
# 📅 北京 春季 一周家庭食谱

> 家庭成员：3人（成人2+儿童1） | 口味：适中不辣 | 生成日期：2026-04-16

## 📋 本周营养概览
- 蛋白质来源：猪肉、鸡肉、鸡蛋、豆腐
- 碳水主食：米饭、面条、馒头
- 蔬菜水果：春笋、菠菜、荠菜、苹果
- 预计成本：200-300元

## 🍽️ 每日食谱详情

### 周一 春笋季
**早餐**：鸡蛋羹、馒头、牛奶
**午餐**：春笋炒肉、清炒菠菜、米饭
**晚餐**：荠菜饺子（孩子爱吃）

（周一至周日完整食谱）

## 🛒 本周采购清单
### 肉蛋类
- 猪肉丝：500g
- 鸡胸肉：300g
- 鸡蛋：20个

### 蔬菜类
- 春笋：3根
- 菠菜：500g
- 荠菜：300g

## ⚠️ 注意事项
- 严格避让海鲜类食材（孩子过敏）
- 儿童餐需清淡少盐
- 春笋需焯水去涩
```

## 安装

### 方式一：OpenClaw（推荐）

通过 ClawHub 安装：

```bash
# 安装 ClawHub CLI
npm install -g clawhub

# 安装 meal-planner skill
clawhub install meal-planner
```

或手动安装：

```bash
# 克隆到 OpenClaw skills 目录
cd ~/.openclaw/skills
git clone https://github.com/skystmm/meal-planner.git
```

安装后 OpenClaw 会自动加载，无需额外配置。

---

### 方式二：Hermes Agent

Hermes Agent 支持导入 OpenClaw skills：

```bash
# 在 Hermes 工作目录
cd ~/hermes-agent/skills

# 克隆 skill
git clone https://github.com/skystmm/meal-planner.git

# Hermes 会自动识别 SKILL.md
```

配置 Hermes Agent 的 skill 目录：

```yaml
# hermes-config.yaml
skills:
  directory: ~/hermes-agent/skills
  auto_load: true
```

---

### 方式三：Claude Code

Claude Code 支持通过 `.claude/skills/` 目录加载：

```bash
# 创建 Claude Code skills 目录
mkdir -p ~/.claude/skills

# 克隆 skill
cd ~/.claude/skills
git clone https://github.com/skystmm/meal-planner.git
```

Claude Code 会自动读取 `SKILL.md` 并应用指令。

---

### 验证安装

安装后可通过以下方式验证：

```bash
# OpenClaw
ls ~/.openclaw/skills/meal-planner/SKILL.md

# Hermes
ls ~/hermes-agent/skills/meal-planner/SKILL.md

# Claude Code
ls ~/.claude/skills/meal-planner/SKILL.md
```

## 技术细节

### 数据来源

- **营养标准**：《中国居民膳食指南（2022）》人民卫生出版社
- **季节食材**：LLM 知识库实时推荐（无需固定文件）

### 依赖

- Python 3.x（可选，用于季节判断脚本）
- 无外部 API 依赖
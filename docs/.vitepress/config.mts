import { defineConfig } from 'vitepress'

const engineeringSidebar = [
  {
    text: '交付策略与分工',
    items: [
      { text: '怎样交付一次软件变化', link: '/engineering/' },
      { text: '工程职责与 AI 分工', link: '/engineering/roles' },
      { text: '产品与需求', link: '/engineering/product' },
      { text: '开发与设计', link: '/engineering/development' },
      { text: '测试与验证', link: '/engineering/testing' },
      { text: '运维与发布', link: '/engineering/operations' },
      { text: 'AI 团队怎样推进项目', link: '/engineering/team' },
      { text: '把握进度与干预', link: '/engineering/management' }
    ]
  },
  {
    text: '策略怎样落在 Git 中',
    items: [
      { text: '从一行变更到共同版本', link: '/start/git' },
      { text: '冲突、版本与发布', link: '/start/git-decisions' }
    ]
  }
]

export default defineConfig({
  lang: 'zh-CN',
  title: '在想法与实现之间',
  description: '从人的视角理解 AI 协作开发',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '写在前面', link: '/start/', activeMatch: '^/start/(?!git)' },
      { text: '工程协作', link: '/engineering/', activeMatch: '^/(engineering/|start/git)' },
      { text: '文档地图', link: '/document-map/' },
      { text: '机制原理', link: '/mechanism/' }
    ],
    sidebar: {
      // Keep the existing Git URLs while placing the examples under engineering.
      '/start/git': engineeringSidebar,
      '/start/': [
        {
          text: '写在前面',
          items: [
            { text: '脑中的那张地图', link: '/start/' },
            { text: '工作中的几个词', link: '/start/concepts' },
            { text: '接下来：怎样交付软件', link: '/engineering/' }
          ]
        }
      ],
      '/engineering/': engineeringSidebar,
      '/document-map/': [
        {
          text: '项目 docs/ 目录',
          items: [
            { text: '目录总览', link: '/document-map/' },
            { text: 'requirements/ · 需求', link: '/document-map/requirements' },
            { text: 'design/ · 体验设计', link: '/document-map/design' },
            { text: 'architecture/ · 技术架构', link: '/document-map/architecture' },
            { text: 'dev/ · 合同与任务', link: '/document-map/dev' },
            { text: 'reports/ · 检查与验收', link: '/document-map/reports' },
            { text: 'control/ · 运行定义', link: '/document-map/control' },
            { text: 'rules/ · 工程规则', link: '/document-map/rules' },
            { text: 'guides/ · 使用说明', link: '/document-map/guides' },
            { text: 'examples/ · 合成示例', link: '/document-map/examples' },
            { text: '从承诺查到证据', link: '/document-map/evidence-chain' }
          ]
        }
      ],
      '/mechanism/': [
        {
          text: '机制原理',
          items: [
            { text: '一项 REQ 的阶段地图', link: '/mechanism/' },
            { text: 'S0～S2 · 意图与设计', link: '/mechanism/intent' },
            { text: 'S3～S5 · 契约与计划', link: '/mechanism/plan' },
            { text: 'S6～S7 · 构建与验证', link: '/mechanism/build-and-check' },
            { text: 'S8～S9 · 调查与修复', link: '/mechanism/investigate-and-repair' },
            { text: 'S10～S11 · 验收与决定', link: '/mechanism/release' },
            { text: '辅助：三份不同的记录', link: '/mechanism/req-identity' },
            { text: '谁推动阶段，凭什么继续', link: '/mechanism/progression' },
            { text: '暂停、修订与下一项需求', link: '/mechanism/lifecycle' }
          ]
        }
      ]
    },
    outline: { label: '本页内容' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '外观',
    lastUpdatedText: '更新于'
  }
})

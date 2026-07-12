#!/bin/bash
cd C:/Users/asp/ai-drama-generator
rm -rf .git
git init
git add -A
git commit -m "feat: AI短剧生成器原型 — HitLens策略验证"
gh repo create one-person-drama-studio --public --description "HitLens策略原型：一人决策，AI执行。2026 AI先锋未来人才大赛参赛作品。" --source=. --remote=origin --push
echo "DONE: $(git remote get-url origin)"

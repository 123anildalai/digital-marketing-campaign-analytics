#!/bin/bash
echo "===================================================="
echo " Uploading Digital Marketing Campaign Analytics to GitHub"
echo " Repository: https://github.com/123anildalai/digital-marketing-campaign-analytics.git"
echo "===================================================="
git init
git add .
git commit -m "feat: complete b.tech major marketing analytics project codebase"
git branch -M main
git remote add origin https://github.com/123anildalai/digital-marketing-campaign-analytics.git
git push -u origin main
echo "===================================================="
echo " Project successfully pushed to GitHub!"
echo "===================================================="

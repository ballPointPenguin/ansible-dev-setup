alias gbh="git branch | head"
alias gloh="git log --oneline --decorate | head"
alias grbsq="git rebase --interactive --autosquash"
alias ncux="npx npm-check-updates"
alias ncui="npx npm-check-updates -u; npm install"
alias nom="rm -rf node_modules; npm cache verify; npm install"
alias nomp="rm package-lock.json; rm -rf node_modules; npm cache verify; npm install"
alias path='echo $PATH | tr -s ":" "\n"'
alias reload="exec $SHELL -l"
alias yom="rm -rf node_modules; yarn cache clean; yarn"
alias zomg="git add . && git stash && git stash drop"
blue='#000DFF'
orange='#FFA200'

autoload -Uz vcs_info
zstyle ':vcs_info:git:*' formats '%r/%b %m%u%c'
zstyle ':vcs_info:git*+set-message:*' hooks git-untracked
zstyle ':vcs_info:*:*' check-for-changes true

+vi-git-untracked(){
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == 'true' ]] && \
        git status --porcelain | grep '??' &> /dev/null ; then
        # This will show the marker if there are any untracked files in repo.
        # If instead you want to show the marker only if there are untracked
        # files in $PWD, use:
        #[[ -n $(git ls-files --others --exclude-standard) ]] ; then
        hook_com[staged]+='T'
    fi
}

setopt PROMPT_SUBST

function git_status() {
	if [[ $(ls -la | tail -n +4 | tr -s ' ' ';' | grep "^.*;.*;.*;.*;.*;.*;.*;.*;.git$") -eq 1 ]]
	then
			PR+="%F{cyan}-%f%F{$blue}[%f%F{cyan}${vcs_info_msg_0_}%f%F{$blue}]%f"
	fi
}

function last_exit() {
	vcs_info
	local LAST_EXIT_CODE=$?
	local PR='
'
	PR+="%F{cyan}┬─┬─%f"
	PR+="%F{$blue}[%f%F{$orange}$USER%f%F{$blue}@%f%F{$orange}$HOST%f%F{$blue}]%f"
	PR+="%F{cyan}:%f%F{$blue}[%f%F{cyan}$($ZSH/custom/plugins/short-pwd.py)%f%F{$blue}]%f"
	PR+="%F{cyan}-%f%F{$blue}[%f%F{cyan}%*%f%F{$blue}]%f"
	PR+="%F{cyan}-%f%F{$blue}[%f%F{cyan}$($ZSH/custom/plugins/exit-code.py $LAST_EXIT_CODE)%f%F{$blue}]%f"
	PR+="%F{cyan}-%f%F{$blue}[%f%F{cyan}${vcs_info_msg_0_}%f%F{$blue}]%f"
	# git_status
	PROMPT="$PR
%F{cyan}  ╰─> λ%f "
}

typeset -a precmd_functions
precmd_functions+=(last_exit)

# git theming
ZSH_THEME_GIT_PROMPT_PREFIX="$fg_bold[green]("
ZSH_THEME_GIT_PROMPT_SUFFIX=")"
ZSH_THEME_GIT_PROMPT_CLEAN="✔"
ZSH_THEME_GIT_PROMPT_DIRTY="✗"

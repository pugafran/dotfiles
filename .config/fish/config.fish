# set quotes "\tAnd one day...\n\t\tI got in" "\tHe who fights for the users" "\tOut there is a new world!\n\t\tOut there is our victory!\n\tOut there is our destiny" "\tI will create the perfect system" "\tNow that is a big door" "\t\t\t\tNow do you know who\n\t\t\t\tthe biggest shareholder is?\n I don't know, some kid?\n\t\t\t\t* shrugs *\n You're Mr. Flynn. Why?\n This is your father's company\n\t\t\t\tNot anymore.\n\t\t\t\t* Jumps *"
set quotes "\tAnd one day...\n\t\tI got in" "\tHe who fights for the users" "\tSometimes to love someone,\n\t\tyou got to be a stranger" "\tDon't let yourself get attached\n\t\tto anything you are not willing\n\tto walk out on in 30 seconds flat\n\t\tif you feel the heat around the corner"

set colors "FB9F1A" "FB9F1A" "FBA0A0" "A0A0FB"

set entry "$(expr $(expr $(date +%s) % $(count $quotes)) + 1)"

set fish_greeting ""

# cd ~
# clear
# neofetch
# echo -e (set_color -i $colors[$entry]) $quotes[$entry] 

alias radeontop='radeontop --transparency --color'
alias c='clear'
alias cc='clear; echo; neofetch; echo -e (set_color -i FB9F1A) $quotes[$(expr $(expr $(date +%s) % $(count $quotes)) + 1)]; echo'
alias l='exa -lah'
alias ..='cd ..'
alias q='exit'
alias btw='neofetch'
alias t='tree -aCh'
alias gap='git add ./;git commit -m "Auto update";git push'
alias col='column -t -s ";"'

#Maintenance
alias kill_orphans='echo; echo "----------KILLING ORPHANS----------";sudo pacman -Qtdq | sudo pacman -Rns -'
alias system_failed='systemctl --failed'
alias journal='sudo journalctl -p 3 -xb'
alias mirrors='echo; echo "----------UPDATING MIRRORS----------"; sudo pacman -S --noconfirm pacman-contrib'
alias upgrade='echo; echo "----------UPDATING & UPGRADING----------"; sudo pacman -Syyuu'
alias keyring='echo; echo "----------UPDATING KEYRING----------"; sudo pacman -S archlinux-keyring'
alias maintenance='keyring; mirrors; upgrade; kill_orphans'
 
#usb
alias usb='sudo mount /dev/sdb1 /media/usb; cd ~/media/usb/; c'

if status is-interactive
    # Commands to run in interactive sessions can go here
end


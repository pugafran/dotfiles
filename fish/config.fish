set quotes "\tAnd one day...\n\t\tI got in" "\tHe who fights for the users" "\tOut there is a new world!\n\t\tOut there is our victory!\n\tOut there is our destiny" "\tI will create the perfect system" "\tNow that is a big door" "\t\t\t\tNow do you know who\n\t\t\t\tthe biggest shareholder is?\n I don't know, some kid?\n\t\t\t\t* shrugs *\n You're Mr. Flynn. Why?\n This is your father's company\n\t\t\t\tNot anymore.\n\t\t\t\t* Jumps *"
set fish_greeting ""
cd ~
clear
neofetch
echo -e (set_color -i FB9F1A) $quotes[$(expr $(expr $(date +%s) % $(count $quotes)) + 1)] 

alias c='clear'
alias cc='clear; echo; neofetch; echo -e (set_color -i FB9F1A) $quotes[$(expr $(expr $(date +%s) % $(count $quotes)) + 1)]; echo'
alias l='ls -la'
alias ..='cd ..'
alias btw='neofetch'
alias lt='tree -A -C'
alias lta='tree -A -a -C'

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


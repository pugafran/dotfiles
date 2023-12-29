#! /bin/sh

echo "Cloning repository. This WILL take a while."
git clone https://www.github.com/alexZeLoCO/dotfiles.git

cp dotfiles/.vim ~/ -drv
cp dotfiles/.config/fish ~/.config/ -drv

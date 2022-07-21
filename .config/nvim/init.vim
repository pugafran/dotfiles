set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching 
set ignorecase              " case insensitive 
set hlsearch                " highlight search 
set incsearch               " incremental search
set tabstop=4               " number of columns occupied by a tab 
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=80                  " set an 80 column border for good coding style
filetype plugin indent on   "allow auto-indenting depending on file type
syntax on                   " syntax highlighting
set mouse=a                 " enable mouse click
set clipboard=unnamedplus   " using system clipboard
filetype plugin on
set cursorline              " highlight current cursorline
set ttyfast                 " Speed up scrolling in Vim

call plug#begin('~/.vim/plugged')
	Plug 'ryanoasis/vim-devicons'
	Plug 'scrooloose/nerdtree'
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

if (has("termguicolors"))
	set termguicolors
endif

let g:NERDTReeShowHidden = 1
let g:NERDTReeMinimalUI = 1
let g:NERDTReeIgnore = []
let g:NERDTReeStatusLine = ''

autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
nnoremap <silent> <C-b> :NERDTreeToggle<CR>

tnoremap <Esc> <C-\><C-n>

set splitright
set splitbelow 

au BufEnter * if &buftype == 'terminal' | :startinsert | endif
function! OpenTerminal ()
	split term://bash
	resize 10
endfunction
nnoremap <c-n> :call OpenTerminal()<CR>

tnoremap <A-h> <C-\><C-n><C-w>h
tnoremap <A-j> <C-\><C-n><C-w>j
tnoremap <A-k> <C-\><C-n><C-w>k
tnoremap <A-l> <C-\><C-n><C-w>l

nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l



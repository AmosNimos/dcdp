#Last Updated: Sat 25 Sep 2021 06:04:17 PM EDT
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)


# Folder path
pico8_path="~/Documents/pico8/pico-8/pico8"
cube2_path="cd ~/Documents/manual_install/sauerbraten/ && ./sauerbraten_unix"

##BASIC BASHRC CONFIG (can be ignored)
#-----
# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
		# We have color support; assume it's compliant with Ecma-48
		# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
		# a case would tend to support setf rather than setaf.)
		color_prompt=yes
    else
		color_prompt=no
    fi
fi
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
#-----

##CUSTUM CONFIG
#-----
# TEXT COLOR CODE VARIABLE
ps_yellow=$'\[\e[0;33m\]'
ps_green=$'\[\e[1;32m\]'
ps_red=$'\[\e[0;91m\]'
ps_blue=$'\[\e[0;94m\]'
ps_white=$'\[\e[0;97m\]'

Yellow=$'\e[0;33m'
Green=$'\e[1;32m'
Red=$'\e[0;91m'
Blue=$'\e[0;94m'
White=$'\e[0;97m'

# TEXT OPTIONS VARIABLE
bold=$'\e[1m'
uline=$'\e[4m'
ps_reset=$'\[\e[0m\]'
Reset=$'\e[0m'

##Line Prompt Statement One
if [ "$color_prompt" = yes ]; then
    PS1="[$ps_red$(date +%H:%M)$ps_reset][$ps_blue\w$ps_reset]:"
else
    PS1='[\w]:'
fi
unset color_prompt force_color_prompt
##Line Prompt Statement One for xterm (the standard terminal emulator)
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="[$ps_red$(date +%H:%M)$ps_reset][$ps_blue\w$ps_reset]:"
    ;;
*)
    ;;
esac

# Use the "top" or the "ps -aux" commands to list the process to terminate and add square braket around the first letter like this [p]rocess.
# With great power comes great responsibility
function hitman(){
	red=$'\e[0;91m'
	reset=$'\e[0m'
	kill_count=1
	echo "$red"
	echo "___    ___     ___     _________     ___        __                    ___    __"
	echo "\ /    \ /     \ /    |/  | |  \|    \  \      / /         /\         \  \   \/"
	echo "| |    | |     | |        | |        |\  \    // |        /. \        ||\ \  ||"
	echo "| |____| |     | |        | |        ||\  \  //| |       // \ \       || \ \ ||"
	echo "| |    | |     | |        | |        || \  \// | |      //___\ \      ||  \ \||"
	echo "| |    | |     | |        | |        ||  \  /  | |     //     \ \     ||   \  |"
	echo "/_\    /_\     /_\        /_\       /_\   \/   /_\    /_\     /__\   /__\   \_|"
	echo
	echo "$1 [TERMINATION]"
	echo
	echo $(ps -aux | grep $1)
	echo
	echo "..."
	echo "[KILL]"
		kill $(ps aux | grep $1 | awk '{print $2}')  || kill_count=0
	
	if [ $kill_count -eq 1 ];then
		echo "$1 [TERMINATED]."
		echo $kill_count
	else 
		clear
		echo "[MISSION FAILED]"
		echo "TARGET STATUS:[ALIVE]"
	fi
	echo "$reset"
}

# some more ls aliases
#alias ll='ls -l'
alias la='ls -A'
#alias l='ls -CF'

export EDITOR='nano'
export VISUAL_EDITOR='gedit'

# My custom alias >>

# Main alias
alias myip="hostname -I | awk '{print $1}'"
alias py="python3"
alias pip="pip3"

# Secondary alias
alias closepc="/sbin/shutdown +0"
alias awerc="$VISUAL_EDITOR ~/.config/awesome/rc.lua"
alias p2t="pdftotext -layout"
alias exe="chmod +x"
alias vioff="set -o emacs"
alias vion="set -o vi"
alias www="bollux"
alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'

# game name
alias supertux="supertux2"
alias editcube="sauerbraten"

# softwair path
alias pico8=$pico8_path
alias cube2=$cube2_path
alias cubelan="sauerbraten-server -nLOCAL_LAN_SERVER -c5 -mmasterserver"

# cd to directory and save directory to temporary history
cds(){
	location=/tmp/cd_history.txt
	cd $1
	if [[ ! -e $location ]]; then
		touch $location
	fi
	echo "$1" >> $location
}


# My function alias >>

# stupid usless programme
cpu(){
	yellow=$'\e[0;33m'
	green=$'\e[1;32m'
	red=$'\e[0;91m'
	reset=$'\e[0m'
	blue=$'\e[0;94m'
	while true; do
		clear
		cpu_usage=$(top -n 1 -b | awk '/^%Cpu/{print int($2)}' )
		echo
		if [ $cpu_usage -lt 10 ]; then
			# Smaller then 10
			echo  "  ╔═══════════╗"
			echo  "  ║ CPU: [$green$cpu_usage%$reset] ║"
			echo  "  ╚═══════════╝" 
			sleep 20
		elif [ $cpu_usage -lt 100 ]; then
			# Larger then 10
			echo  "  ╔════════════╗"
			echo  "  ║ CPU: [$blue$cpu_usage%$reset] ║"
			echo  "  ╚════════════╝"
			sleep 15
		else
			# Larger then 99
			echo  "  ╔═════════════╗"
			echo  "  ║ CPU: [$red$cpu_usage%$reset] ║"
			echo  "  ╚═════════════╝"
			sleep 10
		fi
	done
}

stopwatch(){
	BEGIN=$(date +%s)

	echo Starting Stopwatch...
	echo Press Q to exit.

	while true; do
		NOW=$(date +%s)
		let DIFF=$(($NOW - $BEGIN))
		let MINS=$(($DIFF / 60))
		let SECS=$(($DIFF % 60))
		let HOURS=$(($DIFF / 3600))
		let DAYS=$(($DIFF / 86400))

		# \r  is a "carriage return" - returns cursor to start of line
		printf "\r%3d Days, %02d:%02d:%02d" $DAYS $HOURS $MINS $SECS

	# In the following line -t for timeout, -N for just 1 character
		read -t 0.25 -N 1 input
		if [[ $input = "q" ]] || [[ $input = "Q" ]]; then
	# The following line is for the prompt to appear on a new line.
		    echo
		    break 
		fi
	done
}

memory(){
	#df -BG | sed -n '1p'
	clear
	echo
	df -BG | sed -n '4p'| awk '{print "  Disk name:  [\033[34m" $1 "\033[0m]\n" "  Free space: [" "\033[1;32m" $4 "\033[0m" "/" "\033[1;31m" $2 "\033[0m" "] \n  Used space:" " [\033[1;31m" $3 "\033[0m]" "(\033[34m" $5 "\033[0m)"  }'
	echo
}

bashrc(){
	nohup $VISUAL_EDITOR ~/.bashrc & disown
	sleep 0.5
	clear
}

run(){
	"$1" & disown
	sleep 0.5
	clear
}

#Download youtube video
ytd(){
	#video_folder="/Videos/youtube"
	echo "saving to "$video_folder
	if [ -z "$2" ];then
		#if argument 2 is empty
		youtube-dl --restrict-filenames --output '~/Videos/youtube/%(uploader)s-%(title)s' "$1"
	elif [ $2 == "-q" ]; then
		#cd "/home/l/Documents/global/nohup"
		nohup youtube-dl --restrict-filenames --output '~/Videos/youtube/%(uploader)s-%(title)s' "$1" &> /tmp/nohup.out
		sleep 0.2
		exit
	elif [ $2 == "-sub" ]; then
		youtube-dl --restrict-filenames --write-sub --sub-lang en --output '~/Videos/youtube/%(uploader)s-%(title)s' "$1"
	else
		youtube-dl --restrict-filenames --output '~/Videos/youtube/%(uploader)s-%(title)s' "$1"
	fi
}

# Calculate
calc(){
	echo "$1" | bc
}

#Download audio from youtube video
yt-mp3(){
	dir=~/Music/yt-mp3
	if [[ ! -e $dir ]]; then
		mkdir $dir
	fi
	
	if [ $2 == "-o" ];then
		#if argument 2 is empty
		youtube-dl --restrict-filenames --extract-audio --audio-format 'mp3' --output "$dir/$3/%(title)s.%(ext)s" "$1"
	elif [ $2 == "-q" ]; then
		#cd "/home/l/Documents/global/nohup"
		nohup youtube-dl --restrict-filenames --extract-audio --audio-format 'mp3' --output "$dir/$3/%(title)s.%(ext)s" "$1" &> /tmp/nohup.out
		sleep 0.2
		exit
	else
		echo "Missing argument"
		echo $2
	fi
}

#List video files and play selection
vidl() {
	echo "Historic: $(<~/Videos/historic.txt)"
	line=$(ls -1q | wc -l)
	vid=$(ls | dmenu -p $line)
	if [ $# -eq 0 ]
	then
		mpv --no-sub "$vid" & disown
	else 
		mpv $@ "$vid"& disown
	fi
	echo "$vid" > ~/Videos/historic.txt
	sleep 0.5
	clear
}

# list files/directorys and do X with selection
lsn() {
	line=$(ls -1q | wc -l)
	selection=$(ls | dmenu -p $line)
	$1 $selection $2 
}

#Record screen with sound
recs() {
	dir=~/Videos/recs
	dim=$(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
	echo "$dim"
	if [[ ! -e $dir ]]; then
		mkdir $dir
	else
		ffmpeg -f x11grab -s "$dim" -i :0 -f alsa -i default ~/Videos/recs/$1.mkv || ffmpeg -f x11grab -s "$dim" -i :1 -f alsa -i default ~/Videos/recs/$1.mkv
	fi
}

#Record microphone only
mic() {
	dir=~/Music/mic
	
	# Take a file format as the second argument
	if [ -z "$2" ]; then
		format=".wav"
	else
		format="$2"
	fi
	
	if [[ ! -e $dir ]]; then
		mkdir $dir
	else
		rec ~/Music/mic/$1$format
	fi
}

# Merge images and sound to avi video format
tovid(){
	# ffmpeg -i ep1.png -i ep1.wav ep1.flv
	# ffmpeg -r 1 -loop 1 -i ep1.jpg -i ep1.wav -acodec copy -r 1 -shortest -vf scale=1280:720 ep1.flv
	# ffmpeg -loop 1 -i $Image -i $Audio -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest out.mp4
	Image=$1
	Audio=$2
	Out=$3
	ffmpeg -y -i $Image -i $Audio -c:a copy $Out.avi
}

#Remove spaces in file name
nospace() {
	for f in *\ *; do mv "$f" "${f// /$1}"; done
	#find -name "* *" | sort -rz | while read -d $'\0' f; do mv -v "$f" "$(dirname "$f")/$(basename "${f// /$1}")"; done
}

#Display date and time
clock(){
	yellow=$'\e[0;33m'
	green=$'\e[1;32m'
	red=$'\e[0;91m'
	reset=$'\e[0m'
	blue=$'\e[0;94m'
	counter=0
	old=""
	clear
	echo
	echo "  [$blue$(date +%A" "%d" "%B" "%G)$reset]"
	while true; do
		if [ "$old" != "$(date +%H:%M)" ];then
			echo "  [$red$(date +%r)$reset][$green$counter$reset]" #[$green$(date +%D)$reset]
			old="$(date +%H:%M)"
			counter=$((counter+1))
		fi
		#sleep 30
		
	# In the following line -t for timeout, -N for just 1 character
		read -t 0.25 -N 1 input
		if [[ $input = "q" ]] || [[ $input = "Q" ]]; then
	# Quit the programme.
		    clear
		    break 
		fi
	done
}

#Display time minimalistically
clockmn(){
	yellow=$'\e[0;33m'
	green=$'\e[1;32m'
	red=$'\e[0;91m'
	reset=$'\e[0m'
	blue=$'\e[0;94m'
	counter=1
	old=""
	while true; do
		if [ "$old" != "$(date +%H:%M)" ];then
			clear
			echo
			echo "  [$blue$(date +%m-%d-%y)$reset]"
			echo "  [$red$(date +%H:%M)$reset]" #[$green$(date +%D)$reset]
			old="$(date +%H:%M)"
		fi
	# In the following line -t for timeout, -N for just 1 character
		read -t 0.25 -N 1 input
		if [[ $input = "q" ]] || [[ $input = "Q" ]]; then
	# Quit the programme.
		    clear
		    break 
		fi
	done
}

#Open the terminal path with file manager
go(){
	nohup nautilus . &> /tmp/nohup.out
	sleep 0.2
	exit
}

# turn each line of a text file into the python array format.
makelist(){

	# add the "around each word",
	echo $( cat $1 | sed -e 's/.*/"&",/') > $1

	# remove the last , character
	echo $( cat $1 | sed '$s/.$//') > $1

	# add [ at the start
	sed -i '1i[' $1

	# add [ at the end
	echo $( cat $1 | sed '${s/$/]/}') > $1

	# condense to a single line
	tr -d '\n' < $1
	
	# output the resurling list
	clear
	cat $1
}

# preview hex color in the terminal
show_col() {
    perl -e 'foreach $a(@ARGV){print "\e[48:2::".join(":",unpack("C*",pack("H*",$a)))."m \e[49m "};print "\n"' "$@"
}

# So that ranger memorise the current directory
# Ranger file manager must be installed for this function to work.
#function ranger {
#	local IFS=$'\t\n'
#	local tempfile="$(mktemp -t tmp.XXXXXX)"
#	local ranger_cmd=(
#		command
#		ranger
#		--cmd="map Q chain shell echo %d > "$tempfile"; quitall"
#	)
#	
#	${ranger_cmd[@]} "$@"
#	if [[ -f "$tempfile" ]] && [[ "$(cat -- "$tempfile")" != "$(echo -n `pwd`)" ]]; then
#		cd -- "$(cat "$tempfile")" || return
#	fi
#	command rm -f -- "$tempfile" 2>/dev/null
#}

inside(){
	grep -irl "$1" $(pwd)
}

# list function
lf(){
	echo "Command: go"
	echo "Description: open the terminal path with file manager."
	echo
	echo "Command: clock"
	echo "Description:display date and time"
	echo
	echo "Command: clockmn"
	echo "Description:display date and time in a minimalistic way"
	echo
	echo "Command: nospace"
	echo "Description:replace spaces with argument 1"
	echo "Arguments:symbol"
	echo
	echo "Command: mic"
	echo "Description: record microphone"
	echo
	echo "Command: recs"
	echo "Description: record screen with mirophone"
	echo "Arguments:directory"
	echo
	echo "Command: vidl"
	echo "Description: list file with dmenu and play them with mpv"
	echo "Arguments: -sub"
	echo
	echo "Command: yt-mp3"
	echo "Description: download audio from youtube link"
	echo "Arguments: link(in quote) [-o,-q] directory_name"
	echo
	echo "Command: ytd"
	echo "Description: download video from youtube link"
	echo "Arguments: link(in quote) [-q,-sub] directory_path"
	echo
	echo "Command: makelist"
	echo "Description: convert the lines of a file to a python format array"
	echo "Arguments: file_path"
	echo
	echo "Command: tovid"
	echo "Description: Merge a picture and a sound file to output a video"
	echo "Arguments: Images.format Sound_file.format Output.format"
}

#clear && echo && echo ' \ (•◡•) <[ Hello, World. ]' && echo ""
#clear && echo && echo '  ( ≖.≖) <[ I am watching you. ]' && echo ""
#clear && echo && echo '  t(>.<t) <[ Fuuuuuck! ]' && echo ""
#clear && echo && echo "  ┗ ( ･o･) ┓ <[ it's gnu/linux! ]" && echo
clear && echo -e "🐇 You Take The Red Pill - You Stay In Wonderland, And I Show You How Deep The Rabbit Hole Goes.\n"

#Display date
echo "[$Blue$(date)$Reset]"

# Replace right shift with tild 
	#xmodmap -e 'keycode 62 = 0x007e'
# Replace right control with grave
	#xmodmap -e "keycode 105 = grave"
# Swap caps and escape
	#setxkbmap -option "caps:swapescape"

#chenge the terminal mode from emacs to vi
	#set -o vi
#-----

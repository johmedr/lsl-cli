_lsl_completion()
{
	local cur prev

	cur=${COMP_WORDS[COMP_CWORD]}
	prev=${COMP_WORDS[COMP_CWORD-1]}

	case ${COMP_CWORD} in
		1)
            COMPREPLY=($(compgen -W "list echo show find" -- ${cur}))
			;;
		2)
			case ${prev} in 
				list) _lsl_list_completion ;;
				echo) _lsl_echo_completion ;;
				show) _lsl_show_completion ;;
				find) _lsl_find_completion ;;	
			esac
			;;
		*) 
			COMPREPLY=()
			;;
	esac
}

_lsl_list_completion()
{
	COMPREPLY=($(compgen -W "--all --list --timeout --name --type --source_id --channel_count --channel_format --nominal_srate --hostname --uid --version --session_id --created_at"))
}

_lsl_echo_completion()
{
	_lsl_complete_topics
}

_lsl_show_completion()
{
	_lsl_complete_topics
}

_lsl_find_completion()
{
	_lsl_complete_topics
}

_lsl_complete_topics()
{					
	COMPREPLY=($(lsl list))
}


complete -F _lsl_completion lsl
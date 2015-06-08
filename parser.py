class Parser:
    def parse(self, comment):
        if 'RIP' in comment.body and comment.author.name.lower() != 'f_for_respect':
		return True, 'F'
	elif 'R.I.P.' in comment.body and comment.author.name.lower() != 'f_for_respect':
		return True, 'F'
	elif 'R.I.P' in comment.body and comment.author.name.lower() != 'f_for_respect':
                return True, 'F'
# commenting out code to reply to "F" comments
#	elif comment.body=='F' and comment.author.name.lower() != 'f_for_respect':
#		return True, 'F'
#	if 'rest in peace' in comment.body.lower() and comment.author.name.lower() != 'f_for_respect':
#                return True, 'F'


        else:
            return False, ''

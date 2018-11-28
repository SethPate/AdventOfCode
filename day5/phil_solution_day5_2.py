import md5
from optparse import OptionParser

def replace(string, loc, char):
	s = list(string)
	if s[loc] == '_':
		s[loc] = char
	return "".join(s)

parser = OptionParser()
parser.add_option("-d", "--doorid", dest="doorid", help="Door ID", default="ffykfhsq")
(opts, args) = parser.parse_args()

password = '________'

i = 0
while '_' in password:
	m = md5.new(opts.doorid+str(i))
	digest = m.hexdigest()
	if digest[:5] == '00000' and digest[5].isdigit() and int(digest[5]) < 8:
		password = replace(password, int(digest[5]), digest[6])
		print password
	i += 1

print password

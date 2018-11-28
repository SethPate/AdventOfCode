import md5
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--doorid", dest="doorid", help="Door ID", default="ffykfhsq")
(opts, args) = parser.parse_args()

password = ''

i = 0
while len(password) < 8:
	m = md5.new(opts.doorid+str(i))
	digest = m.hexdigest()
	if digest[:5] == '00000':
		password += digest[5]
		print password
	i += 1

print password

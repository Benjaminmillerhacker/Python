
         /_        _\   /_        _\
        // \      / \\ // \      / \\
        |\__\    /__/| |\__\    /__/|
         \    ||    /   \    ||    /
          \        /     \        /
           \  __  /       \  __  /
   .-""""-. '.__.'.-""""-. '.__.'.-""""-.  /      
 /_        _\|  /_        _\|  /_        _\
// \      / \\ // \      / \\ // \      / \\
|\__\    /__/| |\__\    /__/| |\__\    /__/|
 \    ||    /   \    ||    /   \    ||    /
  \        /     \        /     \        /
   \  __  /       \  __  /       \  __  /
    '.__.'         '.__.'         '.__.'

   π°π»πΈπ΄π½ πΏπ°ππππΎππ³ π±ππππ΄π 







import urllib2
import threading
import Queue
import urllib
threads = 50
target_url = "http://testphp.vulnweb.com"
wordlist_file = "/tmp/all.txt" # from SVNDigger
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101Β¬
 Firefox/19.0"
def build_wordlist(wordlist_file):
 # read in the word list
ο΅ fd = open(wordlist_file,"rb")
 raw_words = fd.readlines()
 fd.close()

 found_resume = False
 words = Queue.Queue()

οΆ for word in raw_words:

 word = word.rstrip()

 if resume is not None:

 if found_resume:
 words.put(word)
 else:
 if word == resume:
 found_resume = True
 print "Resuming wordlist from: %s" % resume

 else:
 words.put(word)

 return words

 def dir_bruter(word_queue,extensions=None):

 while not word_queue.empty():
 attempt = word_queue.get()

 attempt_list = []

 # check to see if there is a file extension; if not,
 # it's a directory path we're bruting
ο΅ if "." not in attempt:
 attempt_list.append("/%s/" % attempt)
 else:
 attempt_list.append("/%s" % attempt)

 # if we want to bruteforce extensions
οΆ if extensions:
 for extension in extensions:
 attempt_list.append("/%s%s" % (attempt,extension))

 # iterate over our list of attempts
 for brute in attempt_list:

 url = "%s%s" % (target_url,urllib.quote(brute))

 try:
 headers = {}
ο· headers["User-Agent"] = user_agent
 r = urllib2.Request(url,headers=headers)


 response = urllib2.urlopen(r)

οΈ if len(response.read()):
 print "[%d] => %s" % (response.code,url)

 except urllib2.URLError,e:
 if hasattr(e, 'code') and e.code != 404:
οΉ print "!!! %d => %s" % (e.code,url)

 pass

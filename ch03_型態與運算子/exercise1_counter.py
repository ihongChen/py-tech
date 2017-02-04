# encoding utf8

import sys

from collections import Counter
cnt = Counter()
for e in sys.argv[2:]:
    cnt[e] += 1

appears = cnt.get(sys.argv[1],0)
print('搜尋的字:{},在句子中出現{}次'.format(sys.argv[1],appears))

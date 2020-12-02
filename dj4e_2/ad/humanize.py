'''
A fucntion to convert the pixels value to natural value(MB, GB)
'''
def natural_size(count):
	k = 1024
	m = k * k
	g = k * m
	fcount = float(count)
	if fcount < k:
		return str(count) + 'B'
	if fcount >= k and fcount < m:
		return str(int(fcount / (k / 10.0 )) / 10.0) + 'KB'
	if fcount >= m and fcount < g:
		return str(int(fcount / (m / 10.0)) / 10.0) + 'MB'
	return str(int(fcount / (g / 10.0)) / 10.0) + 'GB'
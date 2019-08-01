def longestWPI(hours):
        import numpy as np
        hours_np = np.array(hours)
        for i in range(len(hours_np)):
            if hours_np[i]>8:
                hours_np[i]=1
            else:
                hours_np[i]=0
        window_size = len(hours_np)
        best_time = 0
        while window_size>0 and best_time==0:
            for i in range(len(hours_np)):
                if i+window_size<=len(hours_np) and hours_np[i:i+window_size].sum()>window_size/2:
                    best_time = window_size
                    break
            window_size-=1
        print(best_time)
        return best_time
hours=[9,9,6,0,6,6,9]
longestWPI(hours)

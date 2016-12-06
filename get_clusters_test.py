import get_clusters as cluster

def main():
        #cluster.get_clusters_ebv("paul/ebv_human_sorted.MICC", 0)
        #cluster.get_clusters_human("paul/ebv_human_sorted.MICC", 10000)
        cluster.get_clusters_both("paul/ebv_human_sorted.MICC", 200000, 1000)


if __name__ == '__main__':
    main()

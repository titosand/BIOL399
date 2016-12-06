
def separate_by_chrom(path_to_bed):
    result = dict()

    file = open(path_to_bed, 'r').read()
    lines = file.splitlines()
    parsed_lines = [i.split('\t') for i in lines]

    for line in parsed_lines:
        if line[0] not in result.keys() and line[0] != 'chrM':
            result[line[0]] = [line[:6]]
        elif line[0] != 'chrM':
            result[line[0]].append(line[:6])

    return result


def not_duplicate(neighbor, cluster):
    for other in cluster:
        if neighbor[1] == other[1] and neighbor[2] == other[2] and neighbor[4] == other[4] and neighbor[5] == other[5]:
            return False

    return True

def get_clusters_both(path_to_bed, human_range, ebv_range):
    result = dict()

    chromosomes = separate_by_chrom(path_to_bed)

    for c in chromosomes.keys():
        for interaction in chromosomes[c]:
            cluster = []
            for neighbor in chromosomes[c]:
                if is_within_range_both(interaction, neighbor, human_range, ebv_range) and not_duplicate(neighbor, cluster) == True:
                    cluster.append(neighbor)

            if len(cluster) >= 3:
                if c not in result.keys():
                    result[c] = [cluster]
                elif cluster not in result[c]:
                    result[c].append(cluster)

    print_clusters(result)


def is_within_range_both(current, other, human_range, ebv_range):
    if current[1] == other[1] and current[2] == other[2] and current[4] == other[4] and current[5] == other[5]:
        return False

    if abs(int(current[1]) - int(other[1])) > human_range:
        return False

    if abs(int(current[4]) - int(other[4])) > ebv_range:
        return False

    return True

def get_clusters_human(path_to_bed, human_range):
    result = dict()

    chromosomes = separate_by_chrom(path_to_bed)

    for c in chromosomes.keys():
        for interaction in chromosomes[c]:
            cluster = []
            for neighbor in chromosomes[c]:
                if is_within_range_human(interaction, neighbor, human_range) and not_duplicate(neighbor, cluster) == True:
                    cluster.append(neighbor)

            if len(cluster) >= 3:
                if c not in result.keys():
                    result[c] = [cluster]
                elif cluster not in result[c]:
                    result[c].append(cluster)

    print_clusters(result)


def is_within_range_human(current, other, human_range):
    if current[1] == other[1] and current[2] == other[2] and current[4] == other[4] and current[5] == other[5]:
        return False

    if abs(int(current[1]) - int(other[1])) > human_range:
        return False

    return True

def get_clusters_ebv(path_to_bed, ebv_range):
    result = dict()

    chromosomes = separate_by_chrom(path_to_bed)

    for c in chromosomes.keys():
        for interaction in chromosomes[c]:
            cluster = []
            for neighbor in chromosomes[c]:
                if is_within_range_ebv(interaction, neighbor, ebv_range) and not_duplicate(neighbor, cluster) == True:
                    cluster.append(neighbor)

            if len(cluster) >= 5:
                if c not in result.keys():
                    result[c] = [cluster]
                elif cluster not in result[c]:
                    result[c].append(cluster)

    print_clusters(result)


def is_within_range_ebv(current, other, ebv_range):
    if current[1] == other[1] and current[2] == other[2] and current[4] == other[4] and current[5] == other[5]:
        return False

    if abs(int(current[4]) - int(other[4])) > ebv_range:
        return False

    return True

def print_clusters(result):
    total = 0
    for key in result.keys():
        count = 1
        for cluster in result[key]:
            count += 1
            for interaction in cluster:
                print '\t'.join(interaction)
        total += count


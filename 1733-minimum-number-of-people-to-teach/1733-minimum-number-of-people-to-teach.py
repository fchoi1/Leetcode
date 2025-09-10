class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # how many networks basical

        # check each language and each network
        # count how many in the network are connected

        adj_map = defaultdict(set)

        lang = [None] + [set(p_list) for p_list in languages]


        # create networks that friends can't communicate
        for a,b in friendships:
            if lang[a] & lang[b]:
                continue
            adj_map[a].add(b)
            adj_map[b].add(a)


        print(lang, adj_map)


        # loop each language
        # start at friend
        min_count = n
        for i in range(1,n+1):
            count = 0
            print("\n lang", i)
            for curr in adj_map:
                # for other in adj_map[curr]:
                #     if i in lang[other] and i in lang[curr]:
                #         print("error not possible", i, "other", other, "cur", curr)
                #         break
                if i not in lang[curr]:
                    count += 1
                    # elif i not in lang[other] and i not in lang[curr]:
                    #     count += 2
                print("checking", curr, "count", count)
            min_count = min(min_count, count)
                

        return min_count
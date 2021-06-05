class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # Runtime: 452 ms
        # Memory: 22.9 MB
        dishes = set()
        hashmap = {}
        for _, table_number, food in orders:
            hashmap.setdefault(table_number, [])
            hashmap[table_number].append(food)
            dishes.add(food)

        dishes = sorted(dishes)
        hashmap = sorted(hashmap.items(), key=lambda x: int(x[0]))
        table = [["Table"] + dishes]
        for table_number, orders in hashmap:
            row = [table_number]
            for dish in dishes:
                row.append(str(orders.count(dish)))
            table.append(row)
        return table

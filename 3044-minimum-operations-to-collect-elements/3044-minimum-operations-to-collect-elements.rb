# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
    target = k * (k+1) / 2
    seen = Set.new
    curr = 0
    nums.reverse.each_with_index do |n,i|
        next if seen.include?(n) || !(1..k).cover?(n)
        curr += n
        seen.add(n)
        return i + 1 if curr == target
    end
    -1
end
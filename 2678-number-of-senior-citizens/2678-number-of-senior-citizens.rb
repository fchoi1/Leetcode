# @param {String[]} details
# @return {Integer}
def count_seniors(details)
    count = 0
    details.each do |d|
        if d[-4..-3].to_i > 60
            count += 1
        end
    end
    count 
end
# May  8 08:15:01 chewbacca CRON[27954]: pam_unix(cron:session): session opened for user cactiuser by (uid=0)

=begin
a = Hash.new{|h,k| h[k]= Array.new}

File.open("auth.log").each do |line|

    if m = line.match(/(... ..) (..:..:..) chewbacca (\w+)\[\d+\]: (.*)/)
        day, hour, service, s = $1, $2, $3, $4
        a[$2] << "#{day} #{hour}" if ((service != "CRON") and s.match (/.*session (opened|closed) for user (\w+) .*/) )
    end

end

a.keys.each{|p| puts "#{p} #{a[p].size}"}
puts a
=end

class Machin


    def truc(fileName, regex)

        a = []
        File.open(fileName).each do |line|
            a << $1 if line.match(regex)
        end


        a.each{|m1| yield m1}
    end
end

m = Machin.new
m.truc("auth.log", /... .. ..:..:.. chewbacca \w+\[\d+\]: (.*)/)do
    |m|
    puts m
    puts m
end
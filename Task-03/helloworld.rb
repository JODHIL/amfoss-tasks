print "Enter the limit: "
n = gets.chomp.to_i
for i in 2..n
  c = 1
  for j in 2...i
    if i % j == 0
      c = 0
      break
    end
  end
  if c == 1
    print "#{i} "
  end
end

IO.gets("Enter the limit: ") |> String.trim() |> String.to_integer() |> fn n ->
  for i <- 2..n do
    c = 1
    for j <- 2...i do
      if rem(i, j) == 0 do
        c = 0
        break
      end
    end
    if c == 1 do
      IO.write("#{i} ")
    end
  end
end.()

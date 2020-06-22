txt = []
while text = gets do
    txt.push(text)
end

array = txt.join.split(/\n[0-9].*\t/).compact.reject(&:empty?).join(',')
p array
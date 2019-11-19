#!/usr/bin/env ruby
puts ARGV[0]
       .scan(/(\[from:\+?\w+\]|\[to:\+?\d+\]|\[flags:[-1:0]+\])/)
       .join(",")
       .gsub(/(\[from:|\[to:|\[flags:|\])/, '')

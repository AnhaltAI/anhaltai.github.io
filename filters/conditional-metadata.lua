function Meta(m)
  local profiles = quarto.project.profile
  if not profiles then
    -- TODO: missing YAML key? Empty YAML key?..
    -- TODO even more later: filter multiple profiles to use the language one
    return m
  end

  local profile = profiles[1]
  -- If we have a named profile, save it, otherwise return
  if not profile then
    return m
  end

  -- if profile then
  --   print("Profile: " .. profile)
  --   m.active_language = profile
  -- else
  --   return m
  -- end

  if m.titles then
    local titles = m.titles
    if titles[profile] then
      newtitle = pandoc.utils.stringify(titles[profile])
      oldtitle = pandoc.utils.stringify(m.title)
      -- log both if they differ
      if newtitle ~= oldtitle then
        m.title = newtitle
        -- print("Old title:" .. oldtitle)
        -- print("New title:" .. newtitle)
        print(oldtitle .. " => " .. newtitle .. "(" .. profile .. ")")
      end
    else
      print("Title for profile " .. profile .. " not found among ")
      for lang, title in pairs(titles) do -- Table iteration.
        print("    " .. lang .. ": " .. pandoc.utils.stringify(title))
      end
    end
  end

  return m
end

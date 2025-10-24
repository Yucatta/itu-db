import React, { useEffect, useRef, useState } from "react";
interface Props {
  inputRef: React.RefObject<HTMLInputElement | null>;
  setQuery: (value: React.SetStateAction<string | undefined>) => void;
  list: string[];
  placeholder: string;
  query: string;
  onSubmit?: () => void;
}
const InputandList = ({
  inputRef,
  list,
  setQuery,
  onSubmit,
  query,
  placeholder,
}: Props) => {
  const [focusedelement, setfocusedelement] = useState(0);
  const [update, setupdate] = useState(0);
  const listref = useRef<Array<HTMLLIElement | null>>([]);
  useEffect(() => {
    function controlkey(e: KeyboardEvent) {
      if (e.code === "ArrowUp" && focusedelement > 0) {
        setfocusedelement(focusedelement - 1);
      } else if (e.code === "ArrowDown" && focusedelement + 1 < list.length) {
        setfocusedelement(focusedelement + 1);
      } else if (
        (e.code === "Enter" || e.code === "Tab") &&
        list &&
        list.length > 0
      ) {
        if (
          list.filter((statename) => {
            return query.includes(statename);
          })[0]
        ) {
          if (onSubmit) {
            onSubmit();
          }
          inputRef.current!.blur();
        } else {
          setQuery(list[focusedelement]);
          inputRef.current!.value = list[focusedelement];
        }
      } else if (e.code === "Escape") {
        inputRef.current!.blur();
      }
    }
    if (document.activeElement === inputRef.current) {
      addEventListener("keydown", controlkey);
    }
    if (focusedelement >= list.length && focusedelement != 0) {
      setfocusedelement(list.length - 1);
    }
    return () => {
      removeEventListener("keydown", controlkey);
    };
  }, [focusedelement, inputRef.current, list, query, update]);
  useEffect(() => {
    listref.current[focusedelement]?.scrollIntoView({
      block: "nearest",
      behavior: "smooth",
    });
  }, [focusedelement, listref]);
  return (
    <div className="w-full pt-0 relative group" style={{}}>
      <input
        type="search"
        ref={inputRef}
        onChange={() => {
          setQuery(inputRef.current?.value);
        }}
        onClick={() => {
          setupdate(update + 1);
          setfocusedelement(0);
        }}
        onFocus={() => {
          setupdate(update + 1);
          setfocusedelement(0);
        }}
        className="w-full mt-3 h-10 border-2 bg-neutral-900 border-neutral-400 focus-within:"
        placeholder={placeholder}
      />

      <ul className="absolute scrollbar-hide top-full left-0  w-full bg-neutral-900 justify-center  border-2 overflow-y-auto  transition hidden  text-sm z-10 max-h-40 group-focus-within:block">
        {list
          ? list.map((item, index) => (
              <li
                className={
                  focusedelement === index
                    ? "py-1 border-y-2 bg-neutral-600 text-center h-7 text-xs sm:text-base sm:font-semibold cursor-pointer "
                    : "py-1 border-y-2  text-center h-7 text-xs sm:text-base cursor-pointer "
                }
                key={index}
                ref={(el) => {
                  listref.current[index] = el;
                }}
                onMouseEnter={() => {
                  setfocusedelement(index);
                }}
                onMouseDown={() => {
                  setQuery(item);
                  if (inputRef.current) {
                    inputRef.current.value = item;
                  }
                }}
              >
                {item}
              </li>
            ))
          : ""}
      </ul>
    </div>
  );
};

export default InputandList;

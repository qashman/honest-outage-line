# main.py
# make.fun bounty: "The Most Honest Outage Line"
#
# Deterministic, no randomness, no time-based logic, Python 3.13 stdlib only.
# The single printed line must be strictly under 160 characters.

# --- Candidate messages -------------------------------------------------
# Option 1 (dry, deadpan):
#   "All servers are down. The incident channel is very active, mostly with
#    people asking whether the servers are down."                       (110)
#
# Option 2 (smug, self-aware):
#   "Every server is down. This page still loads because it runs on vibes,
#    spite, and one cache we refuse to discuss."                        (105)
#
# Option 3 (chosen - sarcastic, recursive, painfully real):
#   "All servers are down. The engineers are aware, and are currently
#    googling the error message on the servers that are down."           (121)
# ------------------------------------------------------------------------

MESSAGE = (
    "All servers are down. The engineers are aware, and are currently "
    "googling the error message on the servers that are down."
)

LIMIT = 160  # "strictly under 160"


def main() -> None:
    if len(MESSAGE) >= LIMIT:
        raise SystemExit(f"message is {len(MESSAGE)} chars, limit is 159")
    print(MESSAGE, end="")


if __name__ == "__main__":
    main()

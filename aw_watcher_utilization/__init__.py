import argparse

from aw_core.log import setup_logging

from aw_watcher_utilization.watcher import UtilizationWatcher


def main() -> None:
    # Set up argparse
    parser = argparse.ArgumentParser("An Activity Watch watcher which monitors CPU, RAM, GPU and disk usage.")
    parser.add_argument("-v", "--verbose", dest='verbose', action="store_true",
                        help='run with verbose logging')
    parser.add_argument("--testing", action="store_true",
                        help='run in testing mode')
    args = parser.parse_args()

    # Set up logging
    setup_logging("aw-watcher-utilization",
                  testing=args.testing, verbose=args.verbose,
                  log_stderr=True, log_file=True)

    # Start watcher
    watcher = UtilizationWatcher(testing=args.testing)
    watcher.run()


if __name__ == "__main__":
    main()

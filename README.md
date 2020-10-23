# Optimization-409s
### Game Schedule for U.S. National Football League¶
Fall 2020 Optimization

Jianing Zhang, Junyi Qian, Yue Zheng, Ziqiao Yan

NFL is the professional American football league consisting of 32 teams, divided equally between the National Football Conference (NFC) and the American Football Conference (AFC). Each conference is further divided into four division of four clubs and every NFL team is based in the contiguous United States. Since the analysis including all the teams right-away was estimated to be computationally intensive, Liang was asked to develop a preliminary analysis for a subset of teams, namely for teams in the East, North, and South divisions. This setup was agreed by the NFL schedulers to approximate the overall problem sufficiently well to come up with recommendations. Figure 1 shows all the 24 teams that are included in the analysis.

The scheduling of games for the selected subset of teams is constrained by the following four main rules:

1. The season was limited to 12 weeks.
2. Each team would play once per week.
3. All 12 games that a team played would need to be against a different opponent.
4. Each team would play at most six home games (i.e., on their home stadium).


Whereas the overall goal was to reduce the total distance that the teams travelled, there were also other considerations, such as the fairness of the game schedule for all teams and the fairness of the game schedule for broad casting companies. With these thoughts in mind, Liang embarked on the analysis of the NFL game scheduling.

Assignment
In this workshop, you will build an integer programming model and use the results of the optimization to support your recommendations. Make a report of about 3 pages (excluding figures, graphs and appendices) summarizing your results, your interpretation of the results and your conclusions and recommendations. You can include graphs and outputs in an appendix, but make sure to summarize and interpret the results in your report as well.

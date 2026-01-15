const base = {
    get() {
        return {
            url : "http://localhost:8080/python0745x1xa/",
            name: "python0745x1xa",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python的空气质量综合分析系统的设计与实现"
        } 
    }
}
export default base

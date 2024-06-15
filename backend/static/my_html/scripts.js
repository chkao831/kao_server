// Sample data: List of items and their corresponding API endpoints
const base_url = 'http://167.71.138.167:5000/Stock/get_ch_txt'

const items = [
    { name: '《山行》', apis: [
                                ['《山行 6》天塔', `${base_url}/sx_ch6`], 
                                ['《山行 11》热身',`${base_url}/sx_ch11`],
                                ['《山行 13》初罚',`${base_url}/sx_ch13`],
                                ['《山行 17》请罚',`${base_url}/sx_ch17`],
                                ['《山行 19》清账',`${base_url}/sx_ch19`],
                                ['《山行 20》疼痛',`${base_url}/sx_ch20`],
                                ['《山行 27》讨打',`${base_url}/sx_ch27`],
                                ['《山行 28》回家',`${base_url}/sx_ch28`],
                                ['《山行 29》如愿',`${base_url}/sx_ch29`],
                                ['《山行 30》失窃',`${base_url}/sx_ch30`],
                                ['《山行 31》交接',`${base_url}/sx_ch31`],
                                ['《山行 32》道別',`${base_url}/sx_ch32`],
                                ['《山行 34》惩戒期——热身篇',`${base_url}/sx_ch34`],
                                ['《山行 35》惩戒期——告白篇',`${base_url}/sx_ch35`],
                                ['《山行 36》惩戒期——戒尺篇',`${base_url}/sx_ch36`],
                                ['《山行 37》惩戒期——藤条篇',`${base_url}/sx_ch37`],
                                ['《山行 38》惩戒期——刮刀篇-下',`${base_url}/sx_ch38-2`],
                                ['《山行 39》惩戒期——家访篇',`${base_url}/sx_ch39`],
                                ['《山行 40》惩戒期——破皮篇',`${base_url}/sx_ch40`],
                                ['《山行 41》惩戒期——欲望篇',`${base_url}/sx_ch41`],
                                ['《山行 42》惩戒期——尾声',`${base_url}/sx_ch42`],
                                ['《山行 46》旧帐',`${base_url}/sx_ch46`],
                                ['《山行 49》暗桩',`${base_url}/sx_ch49`],
                            ]},
    { name: '《洛夜知秋》- 2024精修', apis: [
                                ['《洛夜知秋 3》星火燎原', `${base_url}/lyzc_ch3`], 
                                ['《洛夜知秋 4》弟子知错', `${base_url}/lyzc_ch4`], 
                                ['《洛夜知秋 5》冰河值得', `${base_url}/lyzc_ch5`], 
                                ['《洛夜知秋 6》清秋认罚', `${base_url}/lyzc_ch6`], 
                                ['《洛夜知秋 7》放过师尊', `${base_url}/lyzc_ch7`], 
                                ['《洛夜知秋 8》慢慢长大', `${base_url}/lyzc_ch8`], 
                                ['《洛夜知秋 9》相形见绌', `${base_url}/lyzc_ch9`], 
                                ['《洛夜知秋 10》我相信他', `${base_url}/lyzc_ch10`], 
                                ['《洛夜知秋 11》中秋家宴', `${base_url}/lyzc_ch11`], 
                                ['《洛夜知秋 12》首次杖刑', `${base_url}/lyzc_ch12`], 
                                ['《洛夜知秋 14》只你一人', `${base_url}/lyzc_ch14`], 
                                ['《洛夜知秋 15》田园交锋', `${base_url}/lyzc_ch15`], 
                                ['《洛夜知秋 16》有幸相遇', `${base_url}/lyzc_ch16`], 
                                ['《洛夜知秋 17》我说了算', `${base_url}/lyzc_ch17`], 
                                ['《洛夜知秋 18》师尊小气', `${base_url}/lyzc_ch18`], 
                                ['《洛夜知秋 19》记忆回廊', `${base_url}/lyzc_ch19`], 
                                ['《洛夜知秋 21》仙陵全刑', `${base_url}/lyzc_ch21`], 
                                ['《洛夜知秋 22》生而为光', `${base_url}/lyzc_ch22`], 
                                ['《洛夜知秋 23》师兄教训', `${base_url}/lyzc_ch23`], 
    ]}
];

document.addEventListener('DOMContentLoaded', () => {
    const itemsList = document.getElementById('itemsList');

    items.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${item.name}</strong><br/>${generateLinks(item.apis)}`;
        itemsList.appendChild(listItem);
    });
});

function generateLinks(apis) {
    return apis.map(api => `<a href="${api[1]}" target="_blank">${api[0]}</a>`).join('<br/>');
}
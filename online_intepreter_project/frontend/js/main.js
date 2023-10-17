const api = {
    v1: {  // api 版本号
        codes: { // api v1 版本下的 code api。
            list: function () { //获取实例查询集
                return '/api/v1/codes/'
            },
            detail: function (pk) { // 获取单一实例
                return `/api/v1/codes/${pk}/`
            },
            create: function () { // 创建实例
                return `/api/v1/codes/`
            },
            update: function (pk) { // 更新实例
                return `/api/v1/codes/${pk}/`
            },
            remove: function (pk) { //删除实例
                return `/api/v1/codes/${pk}/`
            },
            run: function () { //运行代码
                return '/api/v1/codes/run/'
            },
            runSave: function () {// 保存并运行代码
                return '/api/v1/codes/run/?save=true'
            },
            runSpecific: function (pk) { // 运行特定代码实例
                return `/api/v1/codes/run/${pk}/`
            },
            runSaveSpecific: function (pk) { // 运行并保存特定代码实例
                return `/api/v1/codes/run/${pk}/?save=true`
            }
        }
    }
};

let store = {
    list: { //列表状态
        state: undefined,
        changed: false
    },
    detail: { //特定实例状态
        state: undefined,
        changed: false
    },
    output: { //输出状态
        state: undefined,
        changed: false
    }
};

function getInstance(data) {
    if (!data || !data.fields || !data.pk) {
        throw new Error("Invalid data object");
    }
    let instance = data.fields;
    instance.pk = data.pk;
    return instance;
}

//获取 code 列表，更改 list 状态
function getList() {
    $.getJSON({
        url: api.v1.codes.list(),
        success: function (data) {
            store.list.state = data.instances;
            store.list.changed = true;
        }
    })
}

function create(code, name) {
    $.post({
        url: api.v1.codes.create(),
        data: {'code': code, 'name': name},
        dataType: 'json',
        success: function (data) {
            getList();
            alert('保存成功！');
        }
    })
}

function update(pk, code, name) {
    $.ajax({
        url: api.v1.codes.update(pk),
        type: 'PUT',
        data: {'code': code, 'name': name},
        dataType: 'json',
        success: function (data) {
            getList();
            alert('更新成功！');
        }
    })
}

function getDetail(pk) {
    $.getJSON({
        url: api.v1.codes.detail(pk),
        success: function (data) {
            let detail = getInstance(data.instances[0]);
            store.detail.state = detail;
            store.detail.changed = true;
        }
    })
}

function remove(pk) {
    $.ajax({
        url: api.v1.codes.remove(pk),
        type: 'DELETE',
        dataType: 'json',
        success: function (data) {
            getList();
            alert('删除成功！');
        }
    })
}

function run(code) {
    $.post({
        url: api.v1.codes.run(),
        dataType: 'json',
        data: {'code': code},
        success: function (data) {
            let output = data.output;
            store.output.state = output;
            store.output.changed = true;
        }
    })
}
//运行保存代码，并刷新 output 和 list 状态。
function runSave(code, name) {
    $.post({
        url: api.v1.codes.runSave(),
        dataType: 'json',
        data: {'code': code, 'name': name},
        success: function (data) {
            let output = data.output;
            store.output.state = output;
            store.output.changed = true;
            getList();
            alert('保存成功！');
        }
    })
}
//运行特定的代码实例，并刷新 output 状态
function runSpecific(pk) {
    $.get({
        url: api.v1.codes.runSpecific(pk),
        dataType: 'json',
        success: function (data) {
            let output = data.output;
            store.output.state = output;
            store.output.changed = true;
        }
    })
}
//运行并保存特定代码实例，并刷新 output 和 list 状态
function runSaveSpecific(pk, code, name) {
    $.ajax({
        url: api.v1.codes.runSaveSpecific(pk),
        type:'PUT',
        dataType: 'json',
        data: {'code': code, 'name': name},
        success: function (data) {
            let output = data.output;
            store.output.state = output;
            store.output.changed = true;
            getList();
            alert('保存成功！');
        }
    })
}

function flexSize(selector) {
    let ele = $(selector);
    ele.css({
        'height': 'auto',
        'overflow-y': 'hidden'
    }).height(ele.prop('scrollHeight'))
}
//将动态变动大小的动作绑定到输入框上
$('#code-input').on('input', function () {
    flexSize(this)
});

function renderToTable(instance, tbody) {
    let name = instance.name;
    let pk = instance.pk;
    let options = `\
    <button class='btn btn-primary' onclick="getDetail(${pk})">查看</button>\
    <button class="btn btn-primary" onclick="runSpecific(${pk})">运行</button>\
    <button class="btn btn-danger" onclick="remove(${pk})">删除</button>`;
    let child = `<tr><td class="text-center">${name}</td><td>${options}</td></tr>`;
    tbody.append(child);
}

function renderSpecificCodeOptions(pk) {
    let options = `\
    <button class="btn btn-primary" onclick="run($('#code-input').val())">运行</button>\
    <button class="btn btn-primary" onclick=\
    "update(${pk},$('#code-input').val(),$('#code-name-input').val())">保存修改</button>\
    <button class="btn" onclick=\
    "runSaveSpecific(${pk}, $('#code-input').val(), $('#code-name-input').val())">保存并运行</button>\
    <button class="btn btn-primary" onclick="renderGeneralCodeOptions()">New</button>`;
    $('#code-options').empty().append(options);// 先清除之前的选项，再添加当前的选项
}   

function renderGeneralCodeOptions() {
    let options = `\
    <button class="btn btn-primary" onclick="run($('#code-input').val())">运行</button>\
    <button class="btn btn-primary" onclick=\
    "create($('#code-input').val(),$('#code-name-input').val())">保存</button>\
    <button class="btn btn-primary" onclick=\
    "runSave($('#code-input').val(),$('#code-name-input').val())">保存并运行</button>\
    <button class="btn btn-primary" onclick="renderGeneralCodeOptions()">New</button>`;
    $('#code-input').val('');// 清除输入框
    $('#code-output').val('');// 清除输出框
    $('#code-name-input').val('');// 清除代码片段名输入框
    flexSize('#code-output');// 由于我们在改变输入、输出框的内容时并没有出发 ‘input’ 事件，所以需要手动运行这个函数
    $('#code-options').empty().append(options);// 清除的之前的选项，再添加当前的选项
}

function watcher() {
    for (let op in store) {
        switch (op) {
            case 'list':// 当 list 状态改变时就刷新页面中展示 list 的 UI，在这里，我们的 UI 一个 <table> 。
                if (store[op].changed) {
                    let instances = store[op].state;
                    let tbody = $('tbody');
                    tbody.empty();
                    for (let i = 0; i < instances.length; i++) {
                        let instance = getInstance(instances[i]);
                        renderToTable(instance, tbody);
                    }
                    store[op].changed = false; // 记得将 changed 信号改回去哦。
                }
                break;
            case 'detail':
                if (store[op].changed) {// 当 detail 状态改变时，就更新 代码输入框，代码片段名输入框，结果输出框的状态
                    let instance = store[op].state;
                    $('#code-input').val(instance.code);
                    $('#code-name-input').val(instance.name);
                    $('#code-output').val('');// 记得请空上次运行代码的结果哦。
                    flexSize('#code-input');// 同样的，没有出发 'input' 动作，就要手动改变值
                    renderSpecificCodeOptions(instance.pk);// 渲染代码选项
                    store[op].changed = false;// 把 changed 信号改回去
                }
                break;
            case 'output':
                if (store[op].changed) { //当 output 状态改变时，就改变输出框的的状态。
                    let output = store[op].state;
                    $('#code-output').val(output);
                    flexSize('#code-output');// 记得手动调用这个函数。
                    store[op].changed = false // changed 改回去
                }
                break;
        }
    }
}


getList();// 初始化的时候我们应该手动的调用一次，好让列表能在页面上展示出来。
renderGeneralCodeOptions();// 手动调用一次，好让代码选项渲染出来
setInterval("watcher()", 500);// 将 watcher 设置为 500 毫秒，也就是 0.5 秒就执行一次，
// 这样就实现了 UI 在不断的监听状态的变化。
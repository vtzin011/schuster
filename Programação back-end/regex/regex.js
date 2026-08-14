
document.querySelectorAll('.nav-tabs button').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.nav-tabs button').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById('sec' + btn.dataset.section).classList.add('active');
    });
});

function mostrarResultado(id, mensagem, tipo) {
    const el = document.getElementById(id);
    el.textContent = mensagem;
    el.className = 'resultado show ' + tipo;
}

function limparErro(inputId, erroId) {
    document.getElementById(inputId).classList.remove('invalid', 'valid');
    document.getElementById(erroId).classList.remove('show');
    document.getElementById(erroId).textContent = '';
}

function mostrarErro(inputId, erroId, msg) {
    document.getElementById(inputId).classList.add('invalid');
    document.getElementById(inputId).classList.remove('valid');
    const erro = document.getElementById(erroId);
    erro.textContent = msg;
    erro.classList.add('show');
}

function marcarValido(inputId) {
    document.getElementById(inputId).classList.remove('invalid');
    document.getElementById(inputId).classList.add('valid');
}


function validarNome() {
    const valor = document.getElementById('nome').value.trim();
    limparErro('nome', 'nomeErro');

    if (!valor) {
        mostrarErro('nome', 'nomeErro', 'O campo não pode estar vazio.');
        mostrarResultado('nomeResultado', 'Nome inválido', 'erro');
        return;
    }

    const regex = /^[A-Za-zÀ-ÿ\s]+$/;
    if (regex.test(valor)) {
        marcarValido('nome');
        mostrarResultado('nomeResultado', '✓ Nome válido', 'sucesso');
    } else {
        mostrarErro('nome', 'nomeErro', 'O nome deve conter apenas letras e espaços.');
        mostrarResultado('nomeResultado', 'Nome inválido', 'erro');
    }
}


function validarIdade() {
    const valor = document.getElementById('idade').value.trim();
    limparErro('idade', 'idadeErro');

    if (!valor) {
        mostrarErro('idade', 'idadeErro', 'O campo não pode estar vazio.');
        mostrarResultado('idadeResultado', 'Idade inválida', 'erro');
        return;
    }

    const regex = /^\d+$/;
    if (regex.test(valor)) {
        marcarValido('idade');
        mostrarResultado('idadeResultado', '✓ Idade válida', 'sucesso');
    } else {
        mostrarErro('idade', 'idadeErro', 'A idade deve conter apenas números inteiros.');
        mostrarResultado('idadeResultado', 'Idade inválida', 'erro');
    }
}


function validarSenha() {
    const valor = document.getElementById('senha').value;
    limparErro('senha', 'senhaErro');

    if (!valor) {
        mostrarErro('senha', 'senhaErro', 'O campo não pode estar vazio.');
        mostrarResultado('senhaResultado', 'Senha inválida', 'erro');
        return;
    }

    const erros = [];
    if (valor.length < 8) erros.push('pelo menos 8 caracteres');
    if (!/[A-Z]/.test(valor)) erros.push('letra maiúscula');
    if (!/[a-z]/.test(valor)) erros.push('letra minúscula');
    if (!/\d/.test(valor)) erros.push('número');

    if (erros.length === 0) {
        marcarValido('senha');
        mostrarResultado('senhaResultado', '✓ Senha válida', 'sucesso');
    } else {
        const msg = 'Falta: ' + erros.join(', ');
        mostrarErro('senha', 'senhaErro', msg);
        mostrarResultado('senhaResultado', msg, 'erro');
    }
}


function validarCEP() {
    const valor = document.getElementById('cep').value.trim();
    limparErro('cep', 'cepErro');

    if (!valor) {
        mostrarErro('cep', 'cepErro', 'O campo não pode estar vazio.');
        mostrarResultado('cepResultado', 'CEP inválido', 'erro');
        return;
    }

    const regex = /^\d{5}-?\d{3}$/;
    if (regex.test(valor)) {
        marcarValido('cep');
        mostrarResultado('cepResultado', '✓ CEP válido', 'sucesso');
    } else {
        mostrarErro('cep', 'cepErro', 'Formato inválido. Use 99999-999 ou 99999999.');
        mostrarResultado('cepResultado', 'CEP inválido', 'erro');
    }
}


function validarTelefone() {
    const valor = document.getElementById('telefone').value.trim();
    limparErro('telefone', 'telefoneErro');

    if (!valor) {
        mostrarErro('telefone', 'telefoneErro', 'O campo não pode estar vazio.');
        mostrarResultado('telefoneResultado', 'Telefone inválido', 'erro');
        return;
    }

    const regex = /^(\(\d{2}\) \d{5}-\d{4}|\d{11}|\d{2} \d{5}-\d{4})$/;
    if (regex.test(valor)) {
        marcarValido('telefone');
        mostrarResultado('telefoneResultado', '✓ Telefone válido', 'sucesso');
    } else {
        mostrarErro('telefone', 'telefoneErro', 'Formato inválido. Use (45) 99999-9999, 45999999999 ou 45 99999-9999.');
        mostrarResultado('telefoneResultado', 'Telefone inválido', 'erro');
    }
}


function validarCPF() {
    const valor = document.getElementById('cpf').value.trim();
    limparErro('cpf', 'cpfErro');

    if (!valor) {
        mostrarErro('cpf', 'cpfErro', 'O campo não pode estar vazio.');
        mostrarResultado('cpfResultado', 'CPF inválido', 'erro');
        return;
    }

    const regex = /^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$/;
    if (regex.test(valor)) {
        marcarValido('cpf');
        mostrarResultado('cpfResultado', '✓ CPF válido (formato correto)', 'sucesso');
    } else {
        mostrarErro('cpf', 'cpfErro', 'Formato inválido. Use 123.456.789-00 ou 12345678900.');
        mostrarResultado('cpfResultado', 'CPF inválido', 'erro');
    }
}

function extrairNumeros() {
    const texto = document.getElementById('fraseNumeros').value;
    const numeros = texto.match(/\d+/g);

    if (numeros && numeros.length > 0) {
        mostrarResultado('numerosResultado', 'Números encontrados:\n' + numeros.join('\n'), 'sucesso');
    } else {
        mostrarResultado('numerosResultado', 'Nenhum número encontrado na frase.', 'info');
    }
}


function contarVogais() {
    const texto = document.getElementById('fraseVogais').value;
    const vogais = texto.match(/[aeiouáéíóúàèìòùâêîôûãõäëïöüAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜ]/g);
    const qtd = vogais ? vogais.length : 0;
    mostrarResultado('vogaisResultado', `Quantidade de vogais: ${qtd}`, 'sucesso');
}

function contarPalavras() {
    const texto = document.getElementById('frasePalavras').value.trim();
    if (!texto) {
        mostrarResultado('palavrasResultado', 'Quantidade de palavras: 0', 'info');
        return;
    }
    const palavras = texto.match(/\S+/g);
    const qtd = palavras ? palavras.length : 0;
    mostrarResultado('palavrasResultado', `Quantidade de palavras: ${qtd}`, 'sucesso');
}

document.getElementById('formCadastro').addEventListener('submit', function(e) {
    e.preventDefault();
    let valido = true;

    const nome = document.getElementById('cadNome').value.trim();
    limparErro('cadNome', 'cadNomeErro');
    if (!nome || !/^[A-Za-zÀ-ÿ\s]+$/.test(nome)) {
        mostrarErro('cadNome', 'cadNomeErro', 'Nome inválido. Use apenas letras e espaços.');
        valido = false;
    } else {
        marcarValido('cadNome');
    }

    const email = document.getElementById('cadEmail').value.trim();
    limparErro('cadEmail', 'cadEmailErro');
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        mostrarErro('cadEmail', 'cadEmailErro', 'E-mail inválido.');
        valido = false;
    } else {
        marcarValido('cadEmail');
    }

    const tel = document.getElementById('cadTelefone').value.trim();
    limparErro('cadTelefone', 'cadTelefoneErro');
    if (!tel || !/^(\(\d{2}\) \d{5}-\d{4}|\d{11}|\d{2} \d{5}-\d{4})$/.test(tel)) {
        mostrarErro('cadTelefone', 'cadTelefoneErro', 'Telefone inválido. Use (45) 99999-9999, 45999999999 ou 45 99999-9999.');
        valido = false;
    } else {
        marcarValido('cadTelefone');
    }

    const cep = document.getElementById('cadCEP').value.trim();
    limparErro('cadCEP', 'cadCEPErro');
    if (!cep || !/^\d{5}-?\d{3}$/.test(cep)) {
        mostrarErro('cadCEP', 'cadCEPErro', 'CEP inválido. Use 99999-999 ou 99999999.');
        valido = false;
    } else {
        marcarValido('cadCEP');
    }

    const senha = document.getElementById('cadSenha').value;
    limparErro('cadSenha', 'cadSenhaErro');
    const senhaErros = [];
    if (senha.length < 8) senhaErros.push('mínimo 8 caracteres');
    if (!/[A-Z]/.test(senha)) senhaErros.push('letra maiúscula');
    if (!/[a-z]/.test(senha)) senhaErros.push('letra minúscula');
    if (!/\d/.test(senha)) senhaErros.push('número');
    if (senhaErros.length > 0) {
        mostrarErro('cadSenha', 'cadSenhaErro', 'Senha inválida: falta ' + senhaErros.join(', ') + '.');
        valido = false;
    } else {
        marcarValido('cadSenha');
    }

    const confirmar = document.getElementById('cadConfirmar').value;
    limparErro('cadConfirmar', 'cadConfirmarErro');
    if (confirmar !== senha || !confirmar) {
        mostrarErro('cadConfirmar', 'cadConfirmarErro', 'As senhas não coincidem.');
        valido = false;
    } else {
        marcarValido('cadConfirmar');
    }

    if (valido) {
        mostrarResultado('cadastroResultado', '✓ Cadastro realizado com sucesso!', 'sucesso');
    } else {
        mostrarResultado('cadastroResultado', 'Corrija os campos em vermelho antes de continuar.', 'erro');
    }
});


function analisarTexto() {
    const texto = document.getElementById('textoAnalise').value;

    const letras = (texto.match(/[A-Za-zÀ-ÿ]/g) || []).length;
    const numeros = (texto.match(/\d/g) || []).length;
    const palavras = texto.trim() ? (texto.trim().match(/\S+/g) || []).length : 0;
    const vogais = (texto.match(/[aeiouáéíóúàèìòùâêîôûãõäëïöüAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜ]/g) || []).length;
    const espacos = (texto.match(/\s/g) || []).length;
    const especiais = (texto.match(/[^A-Za-zÀ-ÿ0-9\s]/g) || []).length;

    const grid = document.getElementById('statsGrid');
    grid.innerHTML = `
        <div class="stat-item"><div class="num">${letras}</div><div class="label">Letras</div></div>
        <div class="stat-item"><div class="num">${numeros}</div><div class="label">Números</div></div>
        <div class="stat-item"><div class="num">${palavras}</div><div class="label">Palavras</div></div>
        <div class="stat-item"><div class="num">${vogais}</div><div class="label">Vogais</div></div>
        <div class="stat-item"><div class="num">${espacos}</div><div class="label">Espaços</div></div>
        <div class="stat-item"><div class="num">${especiais}</div><div class="label">Especiais</div></div>
    `;
    document.getElementById('analiseResultado').classList.add('show');
}
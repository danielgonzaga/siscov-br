import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-mato-grosso-do-sul',
  templateUrl: './mato-grosso-do-sul.component.html',
  styleUrls: ['./mato-grosso-do-sul.component.css']
})
export class MatoGrossoDoSulComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}

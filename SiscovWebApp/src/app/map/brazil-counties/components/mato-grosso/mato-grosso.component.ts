import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-mato-grosso',
  templateUrl: './mato-grosso.component.html',
  styleUrls: ['./mato-grosso.component.css']
})
export class MatoGrossoComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}

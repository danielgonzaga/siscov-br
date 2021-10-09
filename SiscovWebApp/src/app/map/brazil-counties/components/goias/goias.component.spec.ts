import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GoiasComponent } from './goias.component';

describe('GoiasComponent', () => {
  let component: GoiasComponent;
  let fixture: ComponentFixture<GoiasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GoiasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GoiasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
